from sentence_transformers import SentenceTransformer

#Load the embeeding model once when this file is first imported
#All-MiniLM-L6-v2 turns text into 384 numbers that capture meaning
_model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_text(text: str) -> list[float]:
    """Turn a single piece of text into a list of 384 numbers (a vector)."""
    vector = _model.encode(text)
    return vector.tolist()

def embed_many(texts: list[str]) -> list[list[float]]:
    """Turns many pieces of texts into many vectors, all at once."""
    vectors = _model.encode(texts)
    return [v.tolist() for v in vectors]