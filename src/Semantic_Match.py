import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


class Semantic:
    def __init__(self):
        # Load model
        self.model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
        # Read the embeddings
        self.embeddings = pd.read_pickle("../data/embeddings.p")
        # Load dataset
        self.df = pd.read_csv(
            "../data/source_segments.csv", encoding="latin", sep=";|,", engine="python"
        )

    def find_match(self, input):
        """
        Given the segments, the script search the tree for the best match. First, the cos-sim of the input and the
        average embedding of the roots' subtrees is calculated to reduce the search space
        :param input: The list of audience segments
        :return: dict of best match and the cos-sim score
        """
        # Convert all the segments in the input to a string
        segments = " ".join(input)
        y = self.model.encode(segments)
        label_id, label_name = None, None
        max = 0
        df_first_root = self.df.loc[self.df["label_id_long"] % 10**10 == 0]
        for row in range(len(df_first_root)):
            try:
                # Read the embeddings of the roots, calculate the average of each root's subtree, and compute the cos_sim
                root = df_first_root.iloc[row]["label_name"]
                x = np.mean(
                    self.embeddings[
                        list(
                            self.df.loc[
                                self.df["label_name"].astype(str).str.contains(root)
                            ].index
                        )
                    ],
                    axis=0,
                )
                sim = cosine_similarity([x], [y])[0][0]
                if sim > max:
                    # Update the best result
                    max = sim
                    label_id = df_first_root.iloc[row]["label_id"]
                    label_name = root
            except:
                continue
        # print('root:', label_name)
        df_temp = self.df.loc[self.df["label_id"].astype(str).str[0] == str(label_id)]
        max, which = 0, None
        for i in list(df_temp.index):
            try:
                # Read the embeddings of the filtered source_list and compute the cos_sim
                x = self.embeddings[i]
                sim = cosine_similarity([x], [y])[0][0]
                if sim > max:
                    # Update the best result
                    max = sim
                    which = i
            except:
                continue
        return {"sim": max, **df_temp.loc[which].to_dict()}
