import sys
from urllib.parse import urlparse
from typing import Optional

from .connection import RedisConnection
from .encoders import (
    _encode_simple_string,
    _encode_command_string,
    _encode_array,
    _encode_bulk_string,
    _encode_integer
)
from .parser import RedisParser


class Redis:
    def __init__(
        self,
        connection: RedisConnection
    ):
        self.connection = connection
        self.parser = RedisParser("utf-8")

    @classmethod
    def from_url(cls, connection_uri: str):
        parsed = urlparse(connection_uri)
        netloc = parsed.netloc
        scheme = parsed.scheme
        use_ssl = (str(scheme) == "rediss")

        host, port = tuple(netloc.split(":"))
        conn = RedisConnection(
            host=host,
            port=port,
            ssl=use_ssl
        )

        rds = cls(conn)
        return rds

    async def prepare(self):
        """
        "Prepares" the Redis client for appropriate connections.
        Tries to connect to the socket 5 times.
        """

        tries = 0
        success = False

        if self.connection._open is False:
            while tries != 5 and success is not True:
                # try 5 times
                try:
                    await self.connection.socket_connect()
                except BaseException:
                    # if any exception occurs, increment tries and try to connect again
                    print(f"[Socket Connection Failure] Attempt {tries+1} exhausted. Retrying...", file=sys.stderr)
                    tries += 1
                    success = False
                else:
                    success = True

        if not success:
            host = self.connection.host
            port = self.connection.port
            raise OSError(f"Failed to establish a socket connection after 5 retries to {host}:{port}")

    def command(self, command: str, *args):
        # we will construct an array if any args were provided
        # if any special options were provided such as EX, they will also be properly
        # encoded
        """Generate the appropriate bytes to send across for a command

        :param command: Command Name
        :type command: str
        :return: The encoded bytes (utf-8)
        :rtype: bytes
        """
        no_args = not bool(len(args))
        command = command.upper()

        if no_args:
            command_string = _encode_command_string(command)
        else:
            to_pass_args = [_encode_command_string(command, lonely=False)]
            for arg in args:
                if isinstance(arg, int):
                    parsed_arg = _encode_integer(arg)
                elif isinstance(arg, str):
                    parsed_arg = _encode_bulk_string(arg)

                to_pass_args.append(parsed_arg)
                
            command_string = _encode_array(to_pass_args)

        return command_string.encode("utf-8")

    async def execute_command(self, data: bytes):
        await self.connection.send_message(data)
        return await self.connection.read_message(100)

    async def set(
        self,
        key: str,
        value: str,
        *,
        timeout: Optional[int] = None
    ):
        args = []
        args.append(key)
        args.append(value)

        if timeout:
            args.append("EX")
            args.append(str(timeout))

        command = self.command("SET", *args)
        response = await self.execute_command(command)
        self.parser.parse_message(response)

