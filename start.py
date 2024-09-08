import asyncio

from utils.image_filter_ad import ad_findPhoto
from utils.text_filter_ad import find_similar_texts, #predict | user predict if u need 2 ai

async def main():
    text = await ad_findPhoto("url") # get photo and text in that

    body = await find_similar_texts(
        text=text,
        #candidate_labels=["scam", "spam", "phishing", "job offer", "vacancy"]  -  basic array of labels, find by ai
        #threshold=0.7  -  basic value
    )
    print(body) # (action of ad - job offer and another, percentage or chance - max 1, min 0.7 (theshold in find_similar_texts) )

    # example for text

    text = "" # here ad

    body = await find_similar_texts(
        text=text,
        #candidate_labels=["scam", "spam", "phishing", "job offer", "vacancy"]  -  basic array of labels, find by ai
        #threshold=0.7  -  basic value
    )
    print(body) # (action of ad - job offer and another, percentage or chance - max 1, min 0.7 (theshold in find_similar_texts) )

if __name__ == "__main__":
    asyncio.run(main())
