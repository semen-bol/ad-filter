import asyncio, aiohttp, aiofiles, string, random, os
import pytesseract
from PIL import Image

# Настройка пути к tesseract (если необходимо)
pytesseract.pytesseract.tesseract_cmd = r'C:\введите_свой_путь_до_tesseract-ocr!'

def gennaming(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

async def aiohttp_downloadImg(url: str) -> str | None:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                s = f'{gennaming(20)}.jpg'
                f = await aiofiles.open(f'./utils/image/{s}', mode='wb')
                await f.write(await resp.read())
                await f.close()
                return f"./utils/image/{s}"
            else:
                return None

async def ad_findPhoto(url: str | None) -> bool | None:
    if url != None:
        file = await aiohttp_downloadImg(url)

        i = Image.open(file)
        text = pytesseract.image_to_string(i, "rus") # можете поменять rus на другой нужный вам язык

        os.remove(file)
        return text
    else:
        return None 
    
