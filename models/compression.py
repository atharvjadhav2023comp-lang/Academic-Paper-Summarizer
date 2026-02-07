def compress_text(text, ratio=0.7):
    words = text.split()
    cutoff = int(len(words) * ratio)
    return " ".join(words[:cutoff])
