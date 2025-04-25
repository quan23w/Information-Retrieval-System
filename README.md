
# Information Retrieval System  From Multiple PDF with GoogleGenAI (Gemini)

A Streamlit-based application that allows users to upload PDF documents and ask questions about their content using Google's Generative AI.

## Features

- **PDF Document Processing:**  
    Upload and process multiple PDF documents.

- **Intelligent Retrieval:**  
    Ask questions about document content and get relevant answers.

- **Conversational Interface:**  
    Maintain chat history for contextual follow-up questions.

- **Vector-based Search:**  
    Utilizes FAISS for efficient similarity search on document chunks.

## Architecture

This project implements a Retrieval-Augmented Generation (RAG) pattern with the following components:

### 1.Document Processing Pipeline

- **PDF Text Extraction:**  
    Uses PyPDF2 to extract text from PDF files.

- **Text Chunking:**  
    Employs RecursiveCharacterTextSplitter to divide text into manageable chunks.

- **Embedding Generation:**  
    Leverages Google's embedding model for generating embeddings.

### 2.Vector Database

- **FAISS Vector Store:**  
    Provides efficient similarity search capabilities.

### 3.Question-Answering System

- **Google Gemini AI:**  
    Utilized for natural language processing tasks.

- **Conversational Memory:**  
    Maintains context-aware responses through chat history.
## Installation

1. **Clone the repository**:
    ```
    git clone https://github.com/quan23w/Information-Retrieval-System.git
    cd Information-Retrieval-System
    ```

2. **Set up a virtual environment**:
    ```
    conda create -n genai python=3.9
    conda activate genai
    ```

3. **Install dependencies**:
    ```
    pip install -r requirements.txt
    ```
4. **Create a ```.env``` file with your Google API key**:
    ```
    GOOGLE_API_KEY=your_api_key_here
    ```

## Usage


1. **Start the Application**
    ```
    streamlit run app.py
    ```
    
2. **Upload Documents**
    - Use the sidebar to select one or more PDF files.

    - Click "Submit and Process" to extract text and generate embeddings.

3. **Ask Questions**
    - Type your question in the text input field.
    - The system will retrieve relevant information and generate an answer.
    - Review the conversation history below.

## Requirements

- Python 3.8+
- Google API key with access to Gemini models
- Active internet connection for API access

## License

This project is licensed under the MIT License – see the LICENSE file for details.

## Acknowledgments

- LangChain for document processing and chain management
- Google Generative AI for the language models
- FAISS for efficient vector storage and similarity search
- Streamlit for the web interface