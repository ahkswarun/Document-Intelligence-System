import os
import streamlit as st

from src.rag_setup import get_rag


st.set_page_config(
    page_title="Document Intelligence System",
    page_icon="📚",
    layout="wide"
)


@st.cache_resource(show_spinner=False)
def load_rag(pdf_path):
    return get_rag(pdf_path)


st.title("📚 Document Intelligence System")

st.markdown(
    "Upload any PDF and ask questions grounded in its content."
)

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

if uploaded_file is None:
    st.info("Please upload a PDF to begin.")
    st.stop()


upload_dir = "uploads"
os.makedirs(upload_dir, exist_ok=True)

pdf_path = os.path.join(
    upload_dir,
    uploaded_file.name
)

if not os.path.exists(pdf_path):

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())


try:

    with st.spinner("Loading document..."):

        rag = load_rag(pdf_path)

except Exception as exc:

    st.error("Failed to initialize the RAG system.")
    st.exception(exc)
    st.stop()


question = st.text_input(
    "Ask a question about the document"
)


if st.button("Ask"):

    if not question.strip():

        st.warning("Please enter a question.")

    else:

        with st.spinner("Searching the document..."):

            result = rag.ask(question)

        st.subheader("Answer")
        st.write(result["answer"])

        if result["sources"]:

            st.subheader("📚 Sources")

            for source in result["sources"]:

                with st.expander(f"📄 Page {source['page']}"):

                    st.write(source["preview"])