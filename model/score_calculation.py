from pathlib import Path

import pandas as pd
import numpy as np


class ScoreCalculator:

    def __init__(self):

        df = pd.read_csv('dataset/styles.csv', usecols=range(0, 7))
        most_freq_color = df['baseColour'].value_counts().index[0]
        most_freq_season = df['season'].value_counts().index[0]
        df['baseColour'].fillna(most_freq_color, inplace=True)
        df['season'].fillna(most_freq_season, inplace=True)
        self.df = pd.get_dummies(df, columns=['gender', 'masterCategory', 'subCategory', 'articleType', 'baseColour', 'season'])

    def calculate_precision(self, img1, img2):

        img1_id, img2_id = int(Path(img1).stem), int(Path(img2).stem)
        v1 = np.array(self.df[self.df.id == img1_id])[:, 1:][0]
        v2 = np.array(self.df[self.df.id == img2_id])[:, 1:][0]
        return np.sum(np.dot(v1, v2))/6
