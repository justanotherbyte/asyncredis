from .redis import Redis


async def connect(uri: str) -> Redis:
    """A helper function to parse and prepare a connection from a connection uri string.

    :param uri: Your connection string
    :type uri: str
    :return: A Redis client instance to let you interact with your Redis server
    :rtype: Redis
    """
    redis = Redis.from_url(uri)
    await redis.prepare()
    return redis