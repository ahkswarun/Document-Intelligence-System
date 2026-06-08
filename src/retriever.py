from typing import List, Dict


class Retriever:
    def __init__(self, embedder, vector_store, chunks):
        self.embedder = embedder
        self.vector_store = vector_store
        self.chunks = chunks

    def retrieve(
        self,
        query: str,
        k: int = 5
    ) -> List[Dict]:

        query_embedding = (
            self.embedder.embed_query(query)
        )

        distances, indices = (
            self.vector_store.search(
                query_embedding,
                k
            )
        )

        results = []

        for idx in indices[0]:
            results.append(
                self.chunks[idx]
            )

        return results