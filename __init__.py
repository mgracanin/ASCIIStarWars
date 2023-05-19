from asyncio import sleep
from pathlib import Path

'''
ASCII Art from https://www.asciimation.co.nz/
'''

starwars_file_path = (f"{Path(__file__).parent}/starwars.txt")

async def main():
    LPS = 14 ## Linija po frameu

    with open(starwars_file_path, 'r') as f:
        podaci = f.read().split('\n')
    print('\n' * LPS)
   
    for i in range(0, len(podaci), LPS):
        print("\x1b[{}A\x1b[J{}".format(LPS, '\n'.join(podaci[i + 1:i + LPS])))  # \x1b[{}A\x1b[J pomičemo ESC char 14 linija
        await sleep(int(podaci[i]) * 67 / 1000) ## Delay = 67

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
