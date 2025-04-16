import time
import asyncio

async def func1():
    await asyncio.sleep(2)
    print("1")
    
async def func2():
    await asyncio.sleep(1)
    print("2")
    
async def func3():
    await asyncio.sleep(3)
    print("3")
    
async def main():
    L=await asyncio.gather(
        func1(),
        func2(),
        func3()
        )
asyncio.run(main())
