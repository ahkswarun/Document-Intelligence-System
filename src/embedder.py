from sentence_transformers import SentenceTransformer
from typing import List, Dict
import numpy as np


class Embedder:
    def __init__(self):
        self.model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )
    
    def embed_query(self, query: str):
        return self.model.encode([query])

    def create_embeddings(
        self,
        chunks: List[Dict]
    ) -> np.ndarray:

        texts = [
            chunk["text"]
            for chunk in chunks
        ]

        embeddings = self.model.encode(
            texts,
            show_progress_bar=True
        )

        return embeddings