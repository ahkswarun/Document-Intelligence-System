class RAG:

    def __init__(self,retriever,gemini):
        self.retriever = retriever
        self.gemini = gemini

    def ask(self,question: str):
        chunks = self.retriever.retrieve(question,k=8)
        if not chunks:
            return {
                "answer": "I couldn't find any relevant information in the document.",
                "sources": []
            }
        context = "\n\n".join(chunk["text"] for chunk in chunks)
        
        prompt = f"""
Use ONLY the context below.

Context:
{context}

Question:
{question}

If the answer is not found in the context,
say:
'I could not find that information in the book.'
"""

        answer = self.gemini.generate(prompt)
        sources = []
        seen_pages = set()

        for chunk in chunks:
            if chunk["page"] in seen_pages:
                continue

            seen_pages.add(chunk["page"])
            sources.append(
                {
                    "page": chunk["page"],
                    "preview": chunk["text"][:200].strip() + "..."
                }
            )

        return {
            "answer": answer,
            "sources": sources
        }