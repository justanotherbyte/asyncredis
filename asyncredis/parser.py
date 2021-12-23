from typing import Union

import hiredis


class RedisParser:
    def __init__(
        self,
        encoding: str = "utf-8",
        errors: str = "strict"
    ):
        self.encoding = encoding
        self.reader = hiredis.Reader(encoding=encoding, errors=errors)
        self._handle_errors = errors

    def parse_message(self, message: bytes, *, decode: bool = True) -> Union[str, bytes]:
        # we use hiredis since its a sane and correct redis protocol parser
        # also its very speedy

        # feed the data to hiredis reader
        self.reader.feed(message)
        parsed = self.reader.gets(decode)

        if parsed is False:
            raise ValueError("Incomplete data passed to parser")

        if isinstance(parsed, bytes) and decode is True:
            parsed = parsed.decode(self.encoding, errors=self._handle_errors)

        return parsed