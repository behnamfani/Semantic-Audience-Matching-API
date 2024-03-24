Step-by-step explanation of the model, embedding calculation, approaches, and experiments can be seen in the [notebook](reports/Approaches.ipynb).

## Objective
The objective is to find semantic matches of the encoded descriptions using a language model based on given test audience segments. Subsequently, the cosine similarity between these encoded descriptions and either instance of "label_name" or the merge of "label_name" + "segment_description" is calculated. 

## Exploratory Data Analysis
The "label_name" column contains keywords that can be utilized to find semantic matches. Experiments showed that retaining only 
"label_name" yields more meaningful semantic information compared to merging columns. Upon examining the dataset and the label_ids, it becomes apparent that the dataset forms a tree structure, starting with general topics as the main roots and gradually narrowing down with each child and leaf. Hence, it can be used to make the search space small. Also, the test_audience has descriptions in English and German, which need to be encoded using a multilingual model.


## Model
As a preprocessing step aimed at saving time during inference, the embeddings of df["label_name"] are computed and stored using the 'paraphrase-multilingual-MiniLM-L12-v2' model, which supports text in both English and German. This is a multilingual small Language Model that maps texts to a 384-dimensional dense vector space, 
can be used for tasks such as semantic search, and is suitable for cos-similarity.

## Approach
The main idea is to compare the encoded test segment with the averages of the embeddings of the children of each root. This is because the average embedding captures the more semantic meaning of the subtree. Both the time efficiency 
and performance of this approach were promising, which ultimately led me to choose this method.

## Future works
One future work would be to use different models to get the embeddings as various models may perform differently. Furthermore, more analysis on the dataset and especially its tree structure can be done (e.g. narrow the search space again using "segment_description") to check the balance between runtime and performance.
