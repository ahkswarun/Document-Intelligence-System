import faiss
import numpy as np


class VectorStore:
    def __init__(self, dimension: int):
        self.index = faiss.IndexFlatL2(dimension)

    def add_embeddings(
        self,
        embeddings: np.ndarray
    ):
        self.index.add(
            embeddings.astype(np.float32)
        )

    def search(
        self,
        query_embedding: np.ndarray,
        k: int = 5
    ):
        distances, indices = self.index.search(
            query_embedding.astype(np.float32),
            k
        )

        return distances, indices

    def save(self, path: str):
        faiss.write_index(
            self.index,
            path
        )

    @classmethod
    def load(cls,path: str):
        index = faiss.read_index(path)

        obj = cls(index.d)

        obj.index = index

        return obj