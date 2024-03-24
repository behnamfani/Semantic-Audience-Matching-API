Step-by-step explanation of the model, embedding calculation, approaches, and experiments can be seen in the [notebook](reports/Approaches.ipynb).

## Objective
The objective is to find semantic matches of the encoded descriptions using a language model based on given test audience segments. Subsequently, the cosine similarity between these encoded descriptions and either instances of "label_name" or the merge of "label_name" + "segment_description" is calculated. The "label_name" column contains keywords that can be utilized to find semantic matches. Experiments showed that retaining only 
"label_name" yields more meaningful semantic information compared to merging columns.

## Model
As a preprocessing step aimed at saving time during inference, the embeddings of df["label_name"] are computed and stored using the 'paraphrase-multilingual-MiniLM-L12-v2' model, which supports text in both English and German. This is a multilingual small Language Model that maps texts to a 384 dimensional dense vector space, 
can be used for tasks such as semantic search, and is suitable for cos-similarity.

## Approach
Main idea is comparing the encoded test segment with the averages of the embeddings of the children of each root. This is because the average embedding captures more semantic meaning of the subtree. Both the time efficiency 
and performance of this approach were promising, which ultimately led me to choose this method.
