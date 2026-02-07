from fastapi import APIRouter, UploadFile, File
from fastapi.responses import PlainTextResponse
import os

from utils.pdf_reader import extract_text_from_pdf
from utils.text_cleaner import clean_text
from models.compression import compress_text
from models.tokenizer import chunk_text
from models.summarizer import summarize_text
from config import COMPRESSION_RATIO

router = APIRouter()

UPLOAD_DIR = "data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/summarize", response_class=PlainTextResponse)
async def summarize_pdf(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = extract_text_from_pdf(file_path)
    text = clean_text(text)
    text = compress_text(text, COMPRESSION_RATIO)

    summary = ""
    for chunk in chunk_text(text):
        summary += summarize_text(chunk) + "\n"

    return summary
