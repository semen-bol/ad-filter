import asyncio
import torch

from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

# Инициализация модели для поиска схожих текстов
classifier = pipeline("zero-shot-classification", model="joeddav/xlm-roberta-large-xnli")

async def find_similar_texts(text, candidate_labels=["scam", "spam", "phishing", "job offer", "vacancy"], threshold=0.70):
    try:
        result = await asyncio.to_thread(classifier, text, candidate_labels)

        best_label = result['labels'][0]
        best_score = result['scores'][0]

        # b
        best_score = round(best_score, 2)
        best_score2 = str(best_score)
        a,b = ([int(x)]  for x in best_score2.split(".",1))

        if best_score >= threshold:
            return best_label, b[0]
        else:
            return None, best_score
    except TypeError as err: pass

model_path = "RUSpam/spam_deberta_v4"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)

def predict(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=256)
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class = torch.argmax(logits, dim=1).item()
    return True if predicted_class == 1 else False
