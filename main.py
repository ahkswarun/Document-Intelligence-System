import os
from src.pdf_reader import extract_pdf_text
from src.chunker import create_chunks
from src.embedder import Embedder
from src.vector_store import VectorStore
from src.retriever import Retriever
from src.gemini_client import GeminiClient
from src.rag import RAG
from src.storage import save_chunks, load_chunks

pdf_path = "data/Kalki.pdf"
vectorstore_dir = "vectorstore"
index_path = f"{vectorstore_dir}/book.index"
chunks_path = f"{vectorstore_dir}/chunks.json"

os.makedirs(vectorstore_dir, exist_ok=True)

pages = extract_pdf_text(pdf_path)
print(f"Total pages: {len(pages)}")

if os.path.exists(index_path) and os.path.exists(chunks_path):
    print("Loading existing index...")
    chunks = load_chunks(chunks_path)
    vector_store = VectorStore.load(index_path)
    embeddings = None
else:
    print("Building index...")
    chunks = create_chunks(pages)
    embedder = Embedder()
    embeddings = embedder.create_embeddings(chunks)
    print(embeddings.shape)
    print(type(embeddings))
    print(embeddings[0][:10])

    vector_store = VectorStore(embeddings.shape[1])
    vector_store.add_embeddings(embeddings)
    save_chunks(chunks, chunks_path)
    vector_store.save(index_path)

if embeddings is None:
    embedder = Embedder()

retriever = Retriever(embedder, vector_store, chunks)

gemini = GeminiClient()
rag = RAG(retriever, gemini)


while True:

    question = input("\nAsk a question: ")

    if question.lower() in ["quit", "thank you"]:
        print("Goodbye!")
        break

    answer = rag.ask(question)

    print("\nAnswer:")
    print(answer)
    
