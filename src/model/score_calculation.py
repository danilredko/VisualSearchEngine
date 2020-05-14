from pathlib import Path

import pandas as pd
import numpy as np
from numpy.linalg import norm


class ScoreCalculator:
    """
    A class to represent calculation of scores based on known features provided with dataset

    ...

    Attributes
    __________
    df:
      cleaned data frame with one-hot encoding of gender, masterCategory, subCategory, articleType, etc.

    """
    def __init__(self):

        df = pd.read_csv("dataset/styles.csv", usecols=range(0, 7))
        most_freq_color = df["baseColour"].value_counts().index[0]
        most_freq_season = df["season"].value_counts().index[0]
        df["baseColour"].fillna(most_freq_color, inplace=True)
        df["season"].fillna(most_freq_season, inplace=True)
        self.df = pd.get_dummies(
            df,
            columns=[
                "gender",
                "masterCategory",
                "subCategory",
                "articleType",
                "baseColour",
                "season",
            ],
        )

    def calculate_precision(self, img1, img2):
        """
        Calculates cosine similarity between non visual features
        @param img1: path to image 1
        @param img2: path to image 2
        @return: cosine similarity between two feature vectors
        """

        img1_id, img2_id = int(Path(img1).stem), int(Path(img2).stem)
        v1 = np.array(self.df[self.df.id == img1_id])[:, 1:][0]
        v2 = np.array(self.df[self.df.id == img2_id])[:, 1:][0]

        return np.dot(v1, v2) / (norm(v1)*norm(v2))

