from typing import List, Dict


def create_chunks(
    pages: List[Dict],
    chunk_size: int = 1000,
    overlap: int = 200
) -> List[Dict]:
    """
    Split page text into overlapping chunks.

    Args:
        pages: List of page dictionaries with keys "page" and "text".
        chunk_size: Maximum number of characters per chunk.
        overlap: Number of characters to overlap between successive chunks.

    Returns:
        List of chunk dictionaries with "chunk_id", "page", and "text".
    """

    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")
    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap must be non-negative and smaller than chunk_size")

    chunks = []
    chunk_id = 0

    for page_data in pages:
        page_number = page_data["page"]
        text = page_data["text"]

        start = 0

        while start < len(text):
            end = min(start + chunk_size, len(text))
            chunk_text = text[start:end].strip()

            if not chunk_text:
                break
            if len(chunk_text) < 100 and start != 0:
                break

            chunks.append(
                {
                    "chunk_id": chunk_id,
                    "page": page_number,
                    "text": chunk_text,
                }
            )
            chunk_id += 1
            start += chunk_size - overlap

    print(f"Created {len(chunks)} chunks")
    return chunks