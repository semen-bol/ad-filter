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