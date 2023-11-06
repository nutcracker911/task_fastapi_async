import aiohttp
import asyncio

async def test_concurrency():

    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(3):
            tasks.append(session.get('http://0.0.0.0:80/test'))
        responses = await asyncio.gather(*tasks)
        
        elapsed_times = [await r.json() for r in responses]
        print(elapsed_times)
        for i in range(1, len(elapsed_times)):
        
            if elapsed_times[i]['elapsed'] - elapsed_times[i-1]['elapsed'] >= 3:
                print(elapsed_times[i]['elapsed'] - elapsed_times[i-1]['elapsed'])

if __name__ == '__main__':
    asyncio.run(test_concurrency())