#!/usr/bin/env python

import streamlit as st
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import CTransformers
from langchain.chains import RetrievalQA
from langchain import PromptTemplate

DB_FAISS_PATH = "mylib/vector_db"

# Initialize embeddings and database outside of functions
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2", model_kwargs={"device": "cpu"}
)
db = FAISS.load_local(DB_FAISS_PATH, embeddings)

# Initialize the LLM model once
llm = CTransformers(
    model="TheBloke/Llama-2-7B-Chat-GGML",
    model_type="llama",
    max_new_tokens=512,
    temperature=0.1,
)

custom_prompt_template = """
This is a search engine that returns relevant results based on users query.Users will be able to input prompts based on categories, 
brands, and retailers and receive a list of offers that match their query, along with a similarity score. Always retun offers as a list only give offers available

Context: {context}
Question: {question}

Only return the helpful OFFERS below as a list.
OFFERS:
"""

def set_custom_prompt():
    """
    Prompt template for QA retrieval for each vectorstore
    """
    prompt = PromptTemplate(template=custom_prompt_template, input_variables=['context', 'question'])
    return prompt

def similar_offer(llm, prompt, db):
    """
    Create a RetrievalQA chain for similarity-based offer retrieval
    """
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=db.as_retriever(search_kwargs={"k": 2}),
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt},
    )
    return qa_chain

def generate_response(query):
    """
    Generate a response based on the user query
    """
    qa_prompt = set_custom_prompt()
    qa_result = similar_offer(llm, qa_prompt, db)
    response = qa_result({"query": query})  # Pass the query in a dictionary
    return response

def main():
    st.title("🦜🔗 Fetch Reward Search ChatBot")
    query = st.text_input("Find offers you love!")

        # "Enter" button
    if st.button("Enter"):

        if query:
            response = generate_response(query)
            st.text("Answer:")
            st.write(response["result"])
            
            sources = response["source_documents"]
            if sources:
                st.text("Sources:")
                st.write(sources)
            else:
                st.text("No sources found")

if __name__ == "__main__":
    main()
