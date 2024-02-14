import asyncio
import aiohttp


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.post('http://127.0.0.1:8080/hello/world', json={'message': 'Hello World!'}) as resp:
            print(resp.status)
            print(await resp.text())


asyncio.run(main())