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
    <!-- <a href="">Ubuntu host guide by Digital Ocean.</a> -->
</sup>
</p>

## Information
`asyncredis` is, like I've said above, just a pet-project for me. I really just wanted to experiment with database protocols, and try to write my first database driver!

`asyncredis` internally connects with `asyncio`, allowing for asynchronous socket states. It also supports retrying connections. Please DO NOT use this in production. I recommend `aioredis` for production usage.

#### Internals
Internally, `asyncredis` uses `hiredis` to parse messages that are received from the Redis server. `hiredis` ensures speedy parsing, thanks to being C based.