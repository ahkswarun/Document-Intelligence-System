class RAG:

    def __init__(
        self,
        retriever,
        gemini
    ):
        self.retriever = retriever
        self.gemini = gemini

    def ask(
        self,
        question: str
    ):

        chunks = self.retriever.retrieve(
            question,
            k=8
        )

        context = "\n\n".join(
            chunk["text"]
            for chunk in chunks
        )

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

        return self.gemini.generate(prompt)