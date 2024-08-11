# Ad-Filter
## Start
Фильтр рекламы для Python по тексту и картинке. (async)
C использованием обученой модели ии из ```transformers```, поиск текста на картинке  - ```pytesseract + Pillow```

Перед использованием поиска рекламы через картинку посмотрите файл ```utils/image_filter_ad.py``` в нем есть обязательный к настройке пункт:
``` pytesseract.pytesseract.tesseract_cmd = r'C:\введите_свой_путь_до_tesseract-ocr!' ``` ( там же можно поменять язык, в файле есть помарка, ее легко найти)

Требуется достаточно мощная машина. У меня все работает на кфг rtx 3050 + i5 12400f и 16gb ram где 1гб для пайтона в пике.

start.py:
```python
import asyncio

from utils.image_filter_ad import ad_findPhoto
from utils.text_filter_ad import find_similar_texts

async def main():
    text = await ad_findPhoto("https://url.to_file.ru/file.png") # get photo and text in that

    body = await find_similar_texts(
        text=text,
        #candidate_labels=["scam", "spam", "phishing", "job offer", "vacancy"]  -  basic array of labels, find by ai
        #threshold=0.7  -  basic value
    )
    print(body) # (action of ad, percentage or chance, max 1, min 0.7 (theshold in find_similar_texts) )
if __name__ == "__main__":
    asyncio.run(main())
```
