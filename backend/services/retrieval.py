import chromadb
from backend.utils.embedder import embed_text, embed_many

# Create a ChromaDB client that saves to a folder on disk
# 'chroma_store' is where our vectors will live between runs
_client = chromadb.PersistentClient(path= "chroma_store")

# A 'collection' is like a table - one named bucket of vectors
_collection = _client.get_or_create_collection(name="documents")

def store_chunks(chunks: list[str]) -> int:
    """Embed each chuck and save it in Vector store."""
    vectors= embed_many(chunks)

    # Each chunk needs a unique id. we just number them
    ids = [f"chunk_{i}" for i in range(len(chunks))]

    _collection.add(
        ids = ids,
        documents = chunks,
        embeddings = vectors
    )
    return len(chunks)

def search(question: str, top_k: int = 5) -> list[str]:
    """Find the chunks whose meaning is closest to the question"""
    question_vector = embed_text(question)
    results = _collection.query(query_embeddings=[question_vector], n_results=top_k,)

    # results["documents"] is a list-of-lists; we want the first (and only) list.
    return results["documents"][0]