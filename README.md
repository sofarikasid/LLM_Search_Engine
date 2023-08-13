# LLM Powered Search Engine

[![Fetch Search Engine Continuous Integration](https://github.com/sofarikasid/LLM_Search_Engine/actions/workflows/CI.yml/badge.svg)](https://github.com/sofarikasid/LLM_Search_Engine/actions/workflows/CI.yml)

[![Deploy to huggingface](https://github.com/sofarikasid/LLM_Search_Engine/actions/workflows/CD_Hugging_Face.yml/badge.svg)](https://github.com/sofarikasid/LLM_Search_Engine/actions/workflows/CD_Hugging_Face.yml)

This project aims to develop an intelligent search tool that empowers users to retrieve relevant offers using natural language input. Users will be able to input prompts based on categories, brands, and retailers and receive a list of offers that match their query, along with a similarity score. 
The solution I propose and illustrate is Search and retrieval- Augmented Generation. This makes the system more intelligent, using large language models to respond to user queries (search) not only can users search for offers but also get recommendations and other vital information.
The creation of this LLM-powered search engine encompasses essential steps such as data preparation, feature engineering, embedding, vector space modeling, prompt engineering, and automation through Continuous Integration and Continuous Deployment (CI/CD) practices. All of these processes are facilitated using software design principles and Machine Learning Operations (MLOps) tools and methodologies.

 ### How to Run:
 ```diff
clone repo
$ python -m venv .venv
$ source .venv/bin/activate
$ make install
$ python app.py
```
### Hosted Hugging Face Link
 ```diff
https://huggingface.co/spaces/sofarikasid/LLM_Search_Engine
```

![llm_search_engine_](https://github.com/sofarikasid/LLM_Search_Engine/assets/33644535/d0e8d044-cba8-447c-a2b8-775ae50866d1)
