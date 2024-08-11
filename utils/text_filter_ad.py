import asyncio

from transformers import pipeline

# Инициализация модели для поиска схожих текстов
classifier = pipeline("zero-shot-classification", model="joeddav/xlm-roberta-large-xnli")

async def find_similar_texts(text, candidate_labels=["scam", "spam", "phishing", "job offer", "vacancy"], threshold=0.70):
    try:
        result = await asyncio.to_thread(classifier, text, candidate_labels)

        best_label = result['labels'][0]
        best_score = result['scores'][0]

        if best_score >= threshold:
            return best_label, best_score
        else:
            return None, best_score
    except TypeError as err: print(err); pass