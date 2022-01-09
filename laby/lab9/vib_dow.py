import aiohttp
import asyncio


async def main():

    async with aiohttp.ClientSession() as session:

        pokemon_url = 'https://pokeapi.co/api/v2/pokemon/1'
        async with session.get(pokemon_url) as resp:
            pokemon = await resp.json()
            print(pokemon['name'])

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())