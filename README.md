# Ad-Filter
Фильтр рекламы для Python по тексту и картинке. (async)
C использованием обученой модели ии из ```transformers```, поиск текста на картинке  - ```pytesseract + Pillow```

Перед использованием поиска рекламы через картинку посмотрите файл ```utils/image_filter_ad.py``` в нем есть обязательный к настройке пункт:
``` pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' ```

Требуется достаточно мощная машина. У меня все работает на кфг rtx 3050 + i5 12400f и 16gb ram где 1гб для пайтона в пике.
