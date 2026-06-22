import streamlit as st
from src.rag_setup import get_rag


st.set_page_config(
    page_title="Document Intelligence System",
    page_icon="📚",
    layout="wide"
)


@st.cache_resource(show_spinner=False)
def load_rag():
    return get_rag()


try:
    rag = load_rag()
except Exception as exc:
    st.error("Failed to initialize the RAG app. Please check the model and API setup.")
    st.exception(exc)
    st.stop()


st.title("📚 Document Intelligence System")
st.markdown(
    "Ask questions about the Kalki book and get answers grounded in the Book."
)

question = st.text_input(
    "Ask a question about the book"
)

if st.button("Ask"):

    if not question.strip():
        st.warning("Please enter a question.")
    else:

        with st.spinner("Searching the document..."):

            result = rag.ask(question)

        st.subheader("Answer")
        st.success(result["answer"])

        pages = sorted(
            set(
                chunk["page"]
                for chunk in result["sources"]
            )
        )

        with st.expander("Sources"):

            for page in pages:
                st.write(f"📄 Page {page}")