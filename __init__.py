from asyncio import sleep
from pathlib import Path
import os, sys

'''
ASCII Art from https://www.asciimation.co.nz/
'''

starwars_file_path = (f"{Path(__file__).parent}/starwars.txt")

async def main():
    LPS = 14 ## Lines per frame

    if os.path.exists(starwars_file_path):
        with open(starwars_file_path, 'r') as f:
            podaci = f.read().split('\n')
        print('\n' * LPS)
    else:
        print(f"File {starwars_file_path} does not exist. Make sure file is in the same directory as this script.")
        sys.exit(1)

    for i in range(0, len(podaci), LPS):
        print("\x1b[{}A\x1b[J{}".format(LPS, '\n'.join(podaci[i + 1:i + LPS])))  # \x1b[{}A\x1b[J move ESC char 14 lines
        await sleep(int(podaci[i]) * 67 / 1000) ## Delay = 67

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
