## Storage and Retrival of Image Embeddings using Qdrant Vector Database

<p align='justify'>
A vector database is a type of database optimized for storing and querying multi-dimensional data represented as vectors. We have utilized Qdrant cloud vector database for storing image embeddings created by CLIP in form of vectors. Qdrant calculates the cosine similarity between a given query vector and each vector stored in the database. The database retrieves vectors with the highest cosine similarity values compared to the query vector. These retrieved vectors are then ranked based on their similarity scores, with the most similar vectors appearing higher in the ranked list. This enables quick retrival of article images most similar to the given caption resulting in an efficient text-to-image search. We stored embeddings from the baseline CLIP and finetuned CLIP into two separate databases as described in the notebooks.

For further reading, please use this link - [Qdrant Vector Database](https://qdrant.tech/)
</p>
