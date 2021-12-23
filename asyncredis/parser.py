class RedisParser:
    def __init__(self, encoding: str):
        self.encoding = encoding

    def parse_message(self, message: bytes):
        raw = message.decode(
            encoding=self.encoding, 
            errors="replace"
        )

        byte, response = raw[:1], raw[1:]
        
        if byte not in {
            "*",
            "+",
            ":",
            "-",
            "$"
        }:
            raise RuntimeError("Invalid Protocol byte received, terminating parsing.")

        # if the server returned an error
        if byte == "-":
            return self.parse_error(response)
        # integer
        elif byte == ":":
            response = int(response)
        elif byte == "$":
            length = int(response)
            if length == -1:
                # EMPTY or NULL
                return None
            
            # more parsers coming

    def parse_error(self, response: str):
        raise NotImplementedError(response)
