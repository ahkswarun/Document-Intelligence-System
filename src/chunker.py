from typing import List, Dict


def create_chunks(
    pages: List[Dict],
    chunk_size: int = 1000,
    overlap: int = 200
) -> List[Dict]:
    """
    Split page text into overlapping chunks.
    """

    chunks = []
    chunk_id = 0

    for page_data in pages:

        page_number = page_data["page"]
        text = page_data["text"]

        start = 0

        while start < len(text):

            end = start + chunk_size

            chunk_text = text[start:end]

            chunks.append(
                {
                    "chunk_id": chunk_id,
                    "page": page_number,
                    "text": chunk_text
                }
            )

            chunk_id += 1

            start += chunk_size - overlap

    return chunks