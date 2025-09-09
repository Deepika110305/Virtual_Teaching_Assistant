import streamlit as st
from utils.pdf_processing import extract_text_from_pdf, chunk_text
from utils.search_utils import get_relevant_chunk
from utils.llm_utils import ask_question_to_llm

# --- Streamlit UI ---
st.set_page_config(page_title="Virtual Teaching Assistant", layout="centered")
st.title("📄 Virtual Teaching Assistant: Chat with Your PDF")

uploaded_pdf = st.file_uploader("Upload a PDF file", type=["pdf"])
user_question = st.text_input("Ask a question about this PDF:")

# Maintain chat history
if "history" not in st.session_state:
    st.session_state.history = []

if uploaded_pdf and user_question:
    with st.spinner("Reading PDF..."):
        context_text = extract_text_from_pdf(uploaded_pdf)

    if context_text:
        chunks = chunk_text(context_text, max_chars=1000)
        relevant_chunk = get_relevant_chunk(chunks, user_question)

        with st.spinner("Thinking..."):
            answer = ask_question_to_llm(relevant_chunk, user_question)
            st.session_state.history.append({"question": user_question, "answer": answer})

# Display chat history
for chat in st.session_state.history:
    st.markdown(f"**You:** {chat['question']}")
    st.markdown(f"**Assistant:** {chat['answer']}")
