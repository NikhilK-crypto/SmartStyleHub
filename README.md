# SmartStyleHub

## Introduction
<p align="justify">
The primary objective of this project is to create a user-friendly and efficient platform that simplifies the process of outfit selection by offering personalized style suggestions. Specifically, our system utilizes NLP techniques to interpret user queries, extracting relevant keywords such as occasions ("interview," "casual outing") and clothing preferences ("men," "formal"). Additionally, the system integrates methods to search through a vast database of images featuring clothing items from renowned brands like H&M. By combining these technologies, the system effectively bridges the gap between user queries and visual representations of recommended outfits, offering a seamless and interactive experience. The project focuses on implementing a chatbot-style interface capable of understanding natural language queries related to fashion and providing visually appealing recommendations. The system will prioritize user input, analyzing keywords to identify specific clothing needs and occasions. Moreover, the integration of Computer Vision algorithms will enable the system to retrieve relevant images from the database, showcasing attire from recognized brands such as H&M. However, it's important to note that the system's recommendations will be based solely on the information provided by the user and the available database content. Future iterations of the project may explore additional features, such as real-time image recognition or personalized styling tips based on user preferences and feedback.
<p>

## Requirements 
<p align="justify">
LM Studio - LM Studio is an easy-to-use desktop application designed for experimenting with local and open-source Large Language Models (LLMs). It provides a platform for users to work with LLMs in a local environment. We can download any chat model in LM Studio that is available on Hugging Faces. <p>

link - https://lmstudio.ai/  <p>

llama2 - Doewnload llama2 7B chat model in LM Studio and run it locally. You can create an API for the same to access this on python terminal. 
<p>


## Methodology

<p align='center'><img src="https://github.com/NikhilK-crypto/SmartStyleHub/assets/65084101/03085af8-db2a-4cbc-bbd5-3aa0e761a702" width=65% height=65%/></p>

<p align="justify">
The first phase of the project included leveraging Llama2 as a chat model for the system. We employed text processing techniques and prompt engineering to extract fashion related tokens from the generated response. In the second phase, we focused on leveraging OpenAI's CLIP model to perform text-to-image search which involved passing tokens from chat model as input to get matching fashion article images. The CLIP model was finetuned on H&M dataset containing images and respective captions of for a variety of clothing products. After conducting exploratory data analysis, the data was preprocessed before passing it to the model. We conducted a comparative analysis of performance between the baseline and finetuned CLIP models. Our results showed that the finetuned model had a slightly better R-precision metric score than the base model. CLIP works by creating embeddings of text-image pairs where cosine similarity score is computed to find out closest matching pairs. For efficient storage and retrival of these embeddings we utilized Qdrant vector database. Finally, the Streamlit application for the system provides a user friendly interface where user can ask a fashion query and get relevant suggestions in form of images.
</p>


<p align='center'><img src="https://github.com/NikhilK-crypto/SmartStyleHub/assets/65084101/0afa6a23-699e-413d-abce-b0890dccd893" width=60% height=60%/></p>




For more details check out the project report: 
https://github.com/NikhilK-crypto/SmartStyleHub/blob/main/Report/Project_Report.pdf

