import httpx
import asyncio
from typing import Callable
from typing import Coroutine
import time
addr = "https://langa.pl/crawl/"
# async def crawl0(prefix:str, url:str="")-> None:
#     url =   url or prefix 
#     print(f"Crawling { url }")
#     client = httpx.AsyncClient()
#     try:
#         res = await client.get(url)
#     finally :
#         await client.aclose()
#     for line in res.text.splitlines():
#         if line.startswith(prefix):
#             await crawl0(prefix,line)
# asyncio.run(crawl0("https://langa.pl/crawl/"))


async def progress(url: str,algo: Callable[...,Coroutine]) -> None:
    asyncio.create_task(algo(url),name=url)
    todo.add(url)
    start = time.time()
    while len(todo):
        print(f" {len(todo) }: "+", ".join(sorted(todo)[-3:]))
        await asyncio.sleep(0.5)
    end = time.time()
    print(f"took : {int(end-start)}")


todo = set()

# async  def crawl1(prefix: str, url: str ="") -> None:
#     url = url or prefix
#     client = httpx.AsyncClient()
#     try:
#         res = await client.get(url)
#     finally:
#         await client.aclose()
#     for line in res.text.splitlines():
#         if line.startswith(prefix):
#             todo.add(line)
#             await  crawl1(prefix, line)
#     todo.discard(url) 
# asyncio.run(progress(addr,crawl1))         

async def crawl2(prefix : str, url : str = "")-> None :
    url = url or prefix
    client = httpx.AsyncClient()
    try:
        res = await client.get(url)
    finally:
        await client.aclose()
    for line in res.text.splitlines():
        if line.startswith(prefix):
            todo.add(line)
            asyncio.create_task(crawl2(prefix,line), name = line)
    todo.discard(url)  
asyncio.run(progress(addr,crawl2))   




    




