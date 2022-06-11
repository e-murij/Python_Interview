import aiohttp
import asyncio
import aiofiles

urls_list = ['http://127.0.0.1:8000/', 'http://127.0.0.1:8000/1/', 'http://127.0.0.1:8000/2/']


async def get_url(session, url, i):
    async with session.get(url) as response:
        data = await response.text()
        async with aiofiles.open(f'{i}.txt', mode='w', encoding='utf-8') as f:
            await f.write(data)


async def main(loop):
    async with aiohttp.ClientSession(loop=loop) as session:
        tasks = [get_url(session, url, i) for i, url in enumerate(urls_list)]
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
