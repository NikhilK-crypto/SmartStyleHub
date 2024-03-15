## Streamlit Application

<p align="justify">
The folder contains code files for our Streamlit application. The interface prompts user to select attire section and occasion for which they would like to get outfit suggestions. In the backend, we integrated Llama2 chat model to generate responses which will be passed on to the finetuned CLIP model. The model creates textual embeddings and queries Qdrant vector database, to fetch closest matching image results which are displayed on the UI.

Check out the demo here - [App demo](https://github.com/NikhilK-crypto/SmartStyleHub/blob/main/README.md)
</p>
