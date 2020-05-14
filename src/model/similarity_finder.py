import pickle

import faiss
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

from model.score_calculation import ScoreCalculator


class SimilarityFinder:
    """
    A class to represent an actual similarity finder

    ...

    Attributes
    __________
    filenames:
        list of file names
    image_features:
        features of images
    score_calc:
         refer to ScoreCalculator object
    index:
        built index based on features of images

    """

    def __init__(self):
        self.filenames, self.image_features = SimilarityFinder.read_files()
        self.score_calc = ScoreCalculator()
        self.index = SimilarityFinder.build_index(self.image_features)

    @staticmethod
    def build_index(image_features):
        """
        Builds index based on provided images' features for a fast access
        @param image_features: the features of images
        @return: Index
        """
        index = faiss.IndexFlatIP(image_features.shape[1])
        index.add(image_features)
        return index

    @staticmethod
    def read_files():
        """
        Reads from a file and returns file names and extracted image features
        @return: file names, extracted images' features
        """
        with open("data/filenames.pickle", "rb") as handle:
            filenames = pickle.load(handle)
        image_features = np.load("data/extracted_features.npy")
        return filenames, image_features

    def get_top_k_similar(self, image_name, top_k):
        """
        Return an array of indices of top k similar images to the provided image
        @param image_name: name of image file
        @param top_k: top k indices
        @return: an array of indices of top 5 similar images
        """
        im_index = self.filenames.index(f"images/{image_name}")
        im_feature = np.array([self.image_features[im_index]])
        D, I = self.index.search(im_feature, top_k)

        return I[0]

    def show_top_k(self, image_name: str, top_k: int) -> None:
        """
        Plot top 5 similar images to provided image

        @param image_name: name of image file
        @param top_k: how many images to plot
        @return: None
        """

        I = self.get_top_k_similar(image_name, top_k)
        fig, axs = plt.subplots(1, top_k)
        fig.set_size_inches(25, 15)
        for i, idx in enumerate(I):
            img = mpimg.imread(f"dataset/{self.filenames[idx]}")
            axs[i].imshow(img)
            title = f"Similarity: {self.score_calc.calculate_precision(image_name, self.filenames[idx]):.3f}\nFilename: {self.filenames[idx]}"
            axs[i].set_title(title)
            axs[i].axis("off")
            print(title)

        fig.suptitle(f"Top {top_k} similar images")
        plt.show()
