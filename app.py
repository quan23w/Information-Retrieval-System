import streamlit as st
from src.helpers import *


def user_input(user_question):
    with st.spinner("Thinking..."):
        response = st.session_state.conversation({"question": user_question})
        st.session_state.chatHistory = response["chat_history"]
        for i, message in enumerate(st.session_state.chatHistory):
            if i%2 == 0:
                st.write("User: ", message.content)
            else:
                st.write("Assistant: ", message.content)
def main():
    st.set_page_config("Information Retrieval System", page_icon=":book:", layout="wide")
    st.header("Information Retrieval System ")
    
    user_question = st.text_input("Ask a Question from the PDF documents ")
    
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
        
    if "chatHistory" not in st.session_state:
        st.session_state.chatHistory = None
        
    if user_question:
        user_input(user_question)
        
        
    with st.sidebar:
        st.title("Navigation")
        
        pdf_docs = st.file_uploader("Upload your PDF files and Click on the Submit and Process Button", type="pdf", accept_multiple_files=True)
        
        if st.button("Submit and Process"):
            with st.spinner("Processing..."):
                raw_text = read_pdf(pdf_docs)
                chunks_text = get_chunks_text(raw_text)
                vectors_store = get_vector_store(chunks_text)
                st.session_state.conversation = get_conservational_chain(vectors_store)
                
                st.success("Done")

if __name__ == "__main__":
    main()