from typing import (
    Union,
    Optional
)


CRLF = "\r\n"

def _encode_simple_string(text: str):
    return ("+" + text + CRLF)

def _encode_error(error: str):
    return ("-" + error + CRLF)

def _encode_integer(integer: Union[str, int]):
    integer = str(integer)
    return (":" + integer + CRLF)

def _encode_bulk_string(string: Optional[str]):
    if string is None:
        return "$-1\r\n" # NULL/None as a bulk string.

    length = len(string)
    length = str(length)

    return (
        "$" + length + CRLF + string + CRLF
    )

def _encode_array(array: list):
    length = len(array)
    length = str(length)

    encoded = "*" + length + CRLF
    for i in array:
        encoded += i

    if not encoded.endswith(CRLF):
        encoded += CRLF
    
    return encoded

def _encode_command_string(command: str, lonely: bool = True):
    command = command.upper()

    if lonely:
        return (command + CRLF)
        
    length = len(command)
    return (f"${length}" + CRLF + command + CRLF)