import anthropic
from backend.utils.config import config

# Create one Claude client, wrapped so every call is traced in LangSmith
_client = anthropic.Anthropic(api_key=config.ANTHROPIC_API_KEY)


def generate_answer(question: str, chunks: list[str]) -> str:
    """Ask Claude to answer the question using ONLY the provided chunks."""

    # Join the retrieved chunks into one block of context
    context = "\n\n---\n\n".join(chunks)

    # Build the instruction we send to Claude
    prompt = f"""You are a helpful assistant. Answer the question using ONLY the context below.
If the answer is not in the context, say "I could not find that in the document."

Context:
{context}

Question: {question}

Answer:"""

    # Send it to Claude and get the response
    message = _client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=500,
        messages=[
            {"role": "user", "content": prompt}
        ],
    )

    # Pull the text out of Claude's response
    return message.content[0].text