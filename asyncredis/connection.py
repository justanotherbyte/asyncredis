import asyncio
import ssl
from typing import Optional


class RedisConnection:
    def __init__(self, **options):
        self.host: str = options.pop("host")
        self.port: int = options.pop("port")
        self.using_ssl: bool = options.pop("ssl")

        self.reader: Optional[asyncio.StreamReader] = None
        self.writer: Optional[asyncio.StreamWriter] = None

        self._open = False
    
    async def socket_connect(self):
        """
        Open a TCP socket connection to the Redis server.
        """
        _ssl = None
        if self.using_ssl is True:
            ssl_ctx = ssl.create_default_context()
            _ssl = ssl_ctx

        reader, writer = await asyncio.open_connection(
            host=self.host,
            port=self.port,
            ssl=_ssl
        )

        self.reader = reader
        self.writer = writer

        self._open = True

    async def socket_close(self):
        """
        Close the TCP socket connection, by closing the transport, and closing the writer.
        """
        if self.writer:
            self.writer.transport.close()
            self.writer.close()
            await self.writer.wait_closed()

        self._open = False

    async def send_message(self, blob: bytes):
        """Send a blob of bytes to the Redis server.

        :param blob: The bytes you want to send
        :type blob: bytes
        """
        self.writer.write(blob)
        await self.writer.drain() 
        # flush the writer out after the write
        # preparing it for the next write

    async def read_message(self, n: int = -1) -> bytes:
        """Read from the open IO stream.

        :param n: The number of bytes to read, defaults to -1
        :type n: int, optional
        :return: The bytes read from the IO stream
        :rtype: bytes
        """
        data = await self.reader.read(n)
        return data
