from transformers import pipeline
from config import MAX_SUMMARY_LENGTH

summarizer = pipeline(
    task="text2text-generation",
    model="t5-small"
)

def summarize_text(text):
    result = summarizer(
        "summarize: " + text,
        max_length=MAX_SUMMARY_LENGTH,
        truncation=True,      # ✅ VERY IMPORTANT
        do_sample=False
    )
    return result[0]["generated_text"]
