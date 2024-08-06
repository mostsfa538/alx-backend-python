#!/usr/bin/env python3
""" .... """
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ ... """
    start = asyncio.get_event_loop().time()

    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())

    return (asyncio.get_event_loop().time() - start)
