.. asyncredis documentation master file, created by
   sphinx-quickstart on Sat Dec 25 00:12:29 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to asyncredis's documentation!
======================================

.. automodule:: asyncredis
   :members:
   :undoc-members:
   :show-inheritance:

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Getting Started
================
Getting started with ``asyncredis`` is super easy! Here's some boiler-plate code to get you started!

.. code-block:: python

   import asyncio
   import asyncredis

   async def main():
	redis = await asyncredis.connect("redis://localhost:6345") # connect to your redis server
	await redis.set("hello", "world") # set a key called "hello" with a value of "world"
	value = await redis.get("hello") # retrieve the same key back from the database
	print(value)
	await redis.close() # close and terminate the connection

   loop = asyncio.get_event_loop()
   loop.run_until_complete(main())

.. code-block:: shell

   >>> world


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
