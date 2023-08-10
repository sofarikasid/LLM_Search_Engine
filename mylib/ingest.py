#!/usr/bin/env python
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

def create_vector_db():
    """
    This function creates a vector database 
    """
    # Load CSV data
    loader = CSVLoader(file_path='mylib/combined.csv')
    data = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size = 1000,chunk_overlap=50)
    texts = text_splitter.split_documents(data)
    embeddings= HuggingFaceEmbeddings(model_name= "sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.from_documents(texts,embeddings)
    return db.save_local("mylib/vector_db")


if __name__ == "__main__":
    vector_db = create_vector_db()
    print("Vector database created and indexed.")

