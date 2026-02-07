from utils.pdf_reader import extract_text_from_pdf
from utils.text_cleaner import clean_text
from utils.helpers import ensure_dir
from models.compression import compress_text
from models.tokenizer import chunk_text
from models.summarizer import summarize_text
from config import RAW_DATA_DIR, OUTPUT_DIR, COMPRESSION_RATIO

import os

def main():
    pdf_path = os.path.join(RAW_DATA_DIR, "sample_paper.pdf")

    print("📄 Extracting text...")
    raw_text = extract_text_from_pdf(pdf_path)

    print("🧹 Cleaning text...")
    cleaned_text = clean_text(raw_text)

    print("📉 Compressing text...")
    compressed_text = compress_text(cleaned_text, COMPRESSION_RATIO)

    print("🧠 Generating summary...")
    final_summary = ""

    for chunk in chunk_text(compressed_text):
        final_summary += summarize_text(chunk) + "\n"

    ensure_dir(OUTPUT_DIR)

    output_file = os.path.join(OUTPUT_DIR, "summary.txt")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(final_summary)

    print("✅ Summary saved to:", output_file)

if __name__ == "__main__":
    main()
