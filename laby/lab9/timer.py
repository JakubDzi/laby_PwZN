import asyncio
from rich.console import Console

async def sek_licz():
    await asyncio.sleep(1)

async def main():
    console = Console()
    sek = 0
    min = 0
    while(True):
        await sek_licz()
        sek=sek+1
        if sek>=60:
            min=min+1
            sek=0
        console.clear()
        console.print(f'{min:2.0f}:{sek:2.0f}')

asyncio.run(main())