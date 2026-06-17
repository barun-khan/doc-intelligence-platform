def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 200) -> list[str]:
    """Cut a long string into an overlapping pieces

    chunk_size = how many characters each piece holds.
    overlap = how many character repeats between consutive pieces.
    """
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap
    return chunks