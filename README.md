<h1 align="center">
<sub>
    <img src="https://media.discordapp.net/attachments/822902690010103818/923533249425313792/unknown.png" height="36">
</sub>
&nbsp;
asyncredis
</h1>
<p align="center">
<sup>
An asyncio compatible Redis driver. Just a pet-project.
</sup>
<br>
<sup>
    <a href="https://asyncredis.readthedocs.io/en/latest/">Read the documentation.</a>
</sup>
</p>

## Information
`asyncredis` is, like I've said above, just a pet-project for me. I really just wanted to experiment with database protocols, and try to write my first database driver!

`asyncredis` internally connects with `asyncio`, allowing for asynchronous socket states. It also supports retrying connections. Please DO NOT use this in production. I recommend `aioredis` for production usage.

#### Internals
Internally, `asyncredis` uses `hiredis` to parse messages that are received from the Redis server. `hiredis` ensures speedy parsing, thanks to being C based.

## Examples
If you do decide to test out this driver for yourself, I'll leave some examples below.

```py
import asyncio
import asyncredis


async def main():
    rds = await asyncredis.connect("redis://localhost:6379")
    await rds.set("hello", "world")
    value = await rds.get("hello")
    exists = await rds.exists("hello")
    seralized = await rds.dump("hello")
    await rds.delete("hello")

    print(value)
    print(exists)
    print(seralized)

    await rds.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

```powershell
>>> world
>>> True
>>> b'\x00\x05world\t\x00\xc9#mH\x84/\x11s'
```