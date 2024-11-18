import asyncio
import datetime
def print_now():
    print(datetime.datetime.now())

async def keep_printing(name: str = "") -> None:
    while True:
        print(name, end=" ")
        print_now()
        await asyncio.sleep(1)
# asyncio.run(asyncio.wait_for(keep_printing(),3))
#  but now lets make clearer using  a function as entry point 
async def main()-> None:
    try:
       await asyncio.wait_for(keep_printing("Hey"),3)
    except asyncio.TimeoutError:
        print("oops, error happened")
# asyncio.run(main())

#  Awaitables are just object of classes inherited the  Awaitable class  like Coroutine or  Future
async def main2() -> None:
    kp = keep_printing("hey")
    waiter =  asyncio.wait_for(kp,3)
    try:
        await waiter
    except asyncio.TimeoutError:
        print("time's up")
# asyncio.run(main2())

async def main3() -> None:
    await keep_printing("hey")
    await keep_printing("hey2")
# asyncio.run(main3())

# using the gather to register all the coroutins in the same moment in the event loop 
async def main4() -> None:
    task1=  keep_printing("hey")
    task2 = keep_printing("hey2")
    gather = asyncio.gather(task1,task2)
    await asyncio.wait_for(gather,3)
    
    print(type(gather))

# asyncio.run(main4())
#  But the above code gives Cancel Error  the cancel error arise from the  asyncio.sleep

async def keep_printing2(name: str = "") -> None:
    while True:
        print(name, end=" ")
        print_now()
        try:
         await asyncio.sleep(1)
        except asyncio.CancelledError:
         print(f"ops {name} is canceled ")
         break

async def main5() -> None:
    task1=  keep_printing2("hey")
    task2 = keep_printing2("hey2")
    gather = asyncio.gather(task1,task2)
    await asyncio.wait_for(gather,3)
asyncio.run(main5())



#  Coroutine object can ONLY awaited ONCE     

# Helpful for Debugging
PYTHONASYNCIODEBUG = 1
PYTHONTRACEMALLOC = 1

    
