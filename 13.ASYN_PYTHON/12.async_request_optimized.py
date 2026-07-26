from base64 import standard_b64decode
import aiohttp 
import asyncio
import time

async def fetch_page(session, url): # async def — indica que es una corrutina, puede pausarse con await mientras espera la respuesta del servidor
    page_start = time.time()
    async with session.get(url) as response:
        #print(response.status)
        print(f'the page took {time.time() - page_start}')
        return response.status

async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp().ClientSession(loop = loop) as session: #pasamos el loop como forma pa asegurarnos que estamos usando el mismo loop que creamos antes
        for url in urls: 
            tasks.append(fetch_page(session,url))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks


loop = asyncio.get_event_loop()

urls = ['http://google.com' for i in range(50)]
start = time.time()
loop.run_until_complete(get_multiple_pages(loop, *urls))
print(f'all requests took {time.time() - start}')

