# this will be the entry point for the web search queries

from ddgs import DDGS
import aiohttp
import asyncio
import requests
from trafilatura import extract
# contentResult = ""

async def getContents(session, link):
    async with session.get(link) as response:
        return await response.text()

async def test():
    results = DDGS().text("Where is canada located", max_results=5)
    links = [x['href'] for x in results]
    print(links)

    async with aiohttp.ClientSession() as session:
        tasks = [getContents(session,link) for link in links]
        contentResults = await asyncio.gather(*tasks)
    for content in contentResults:
        print("--------------------------------")
        print(extract(content))
        print("--------------------------------")

asyncio.run(test())

