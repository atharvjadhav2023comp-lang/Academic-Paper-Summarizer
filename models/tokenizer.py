def chunk_text(text, max_words=300):
    """
    300 words ≈ <512 tokens for T5/BART-style models
    """
    words = text.split()
    for i in range(0, len(words), max_words):
        yield " ".join(words[i:i + max_words])
