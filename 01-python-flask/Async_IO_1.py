# Asynchronous I/O, or async for short, is a programming pattern that allows for high-performance I/O operations in a concurrent and non-blocking manner.
#  In Python, async programming is achieved through the use of the asyncio module and asynchronous functions.
import asyncio, time

async def function_1():
    await asyncio.sleep(1)
    print("My function 1")
    return 

async def function_2():
    await asyncio.sleep(1)
    print("My function 2")
    return

async def function_3():
    await asyncio.sleep(4)
    print("My function 3")
    return

async def main():
    # asyncio.create_task(function_1())
    # # await function_1()
    # await function_2()
    # await function_3()

    # asyncio.run(main())
    L=await asyncio.gather(
    function_1(),
    function_2(),
    function_3()
    )
    print(L)

# import asyncio
# async def my_async_function():
#     # asynchronous code here
#     await asyncio.sleep(1)
#     return "Hello, Async World!"

# async def main():
#     result = await my_async_function()
#     print(result)

# asyncio.run(main())