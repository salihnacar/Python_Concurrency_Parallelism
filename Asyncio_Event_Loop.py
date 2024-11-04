import asyncio
loop = asyncio.get_event_loop()
loop.set_debug(True)

# the loop is just gonna run forever 
# loop.run_forever()

# another loop waiting the completion of other tasks
# we should keep in mind that the asyncio.sleep is non blocking routine that differs 
# the standart sleep 
# loop.run_until_complete(asyncio.sleep(5))

import  datetime
def print_now():
    print(datetime.datetime.now())
# # we can schedule the execution like that 
# # so now when the loop is run it will see the soon to be executed tasks and execute them
# loop.call_soon(print_now)
# loop.call_soon(print_now)
# loop.run_until_complete(asyncio.sleep(5)) 


# the Trampoline code is when a call back function run and re register itself to run again  like a ball repeatedly bouncing on a trampoline
def trampoline(name : str = ""):
    print(name , end="")
    print_now()
    loop.call_later(0.5,trampoline,name)
#  this fuction will run the trampoline as soon as possible while the other will stop the loop after 8 seconds
# loop.call_soon(trampoline)
# loop.call_later(8,loop.stop)
# loop.run_forever()

#  we also can run multiple trumpoline at the same time 
loop.call_soon(trampoline,"first")
loop.call_soon(trampoline,"second")
loop.call_soon(trampoline,"third")
#  to demonstrate that they are not running at true parallelism we schudule heavy  cpu_bound function to run 

def hog():
    sum = 0
    print("the hog is running")
    for i in range(10_000):
        for j in range(10_000):
            sum += j
    print("the hog is finished")
    return sum
loop.call_later(15,hog)
loop.call_later(25,loop.stop)
loop.run_forever()
