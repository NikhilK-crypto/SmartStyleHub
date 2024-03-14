## Finetuning and Evaluating CLIP

<p align="justify">
In above file we finetuned CLIP model with the H&M dataset for 4 epochs, with a small learning rate of 0.000005 and cross entropy loss. To compare performances of the baseline and finetuned models, we used R-precision metric using cosine similarity between image and text embeddings as follows: Calculate how similar the model thinks images and their true captions (matching pairs) are and how different images and rest of the image captions (non-matching pairs) are. This R-precision was computed for both whole test data and test data segregated by product type and color name. Our results showed that the finetuned model had a slightly better R-precision metric score than the base model.

For detailed results please see the project report here - [Project Report](https://github.com/NikhilK-crypto/SmartStyleHub/blob/main/Report/Project_Report.pdf)
</p>
