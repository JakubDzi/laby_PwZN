import aiohttp
import asyncio


async def main():

    async with aiohttp.ClientSession() as session:

        pokemon_url = 'https://pokeapi.co/api/v2/pokemon/'
        for i in range (10):
            async with session.get((pokemon_url+str(i+1))) as resp:
                pokemon = await resp.json()
                print(pokemon['name'])

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())