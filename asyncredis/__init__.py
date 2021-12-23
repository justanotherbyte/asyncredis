__version__ = "1.0.0a"
__author__ = "justanotherbyte"

from .redis import Redis
from .connection import RedisConnection


async def connect(uri: str) -> Redis:
    rds = Redis.from_url(uri)
    await rds.prepare()
    return rds