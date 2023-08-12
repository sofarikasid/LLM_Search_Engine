#!/usr/bin/env python

from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import CTransformers

# from langchain.chains import RetrievalQA
# from langchain import PromptTemplate

DB_FAISS_PATH = "mylib/vector_db"

# Initialize embeddings and database outside of functions
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2", model_kwargs={"device": "cpu"}
)
db = FAISS.load_local(DB_FAISS_PATH, embeddings)

# Initialize the LLM model once
llm = CTransformers(
    model="TheBloke/Llama-2-7B-Chat-GGML",
    # model= "meta-llama/Llama-2-7b-chat-hf".
    model_type="llama",
    max_new_tokens=512,
    temperature=0.5,
)

# Initialize the QA chain once
# qa = RetrievalQA.from_chain_type(llm=llm, chain_type='stuff', retriever=db.as_retriever(search_kwargs={'k': 10}), return_source_documents=True)
#retriever = db.as_retriever(search_kwargs={"k": 10})


def final_result(query):
    docs_and_scores = db.similarity_search_with_score(query,k=10)
    #response = retriever.get_relevant_documents(query)
    return docs_and_scores


if __name__ == "__main__":
    while True:
        user_query = input(
            "Please enter Retailer, Brand, or Category (type 'exit' to quit): "
        )
        if user_query == "exit":
            break
        llm_response = final_result(user_query)

        print(llm_response)
