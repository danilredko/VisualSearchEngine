import os

import tensorflow as tf
import tensorflow_hub as hub
import numpy as np


class FeatureExtractor:
    """
    A class to represent feature extractor

    ...

    Attributes
    __________
    model:
        contains the pre-trained model loaded from tensorflow-hub

    """
    def __init__(self, config):
        """
        Constructs all the necessary attributes for Feature Extractor model and builds it
        @param config: contains all necessary parameters needed to define and build a model
        """
        self.model = tf.keras.Sequential(
            [hub.KerasLayer(config["url"], trainable=False,),]
        )
        self.model.build(
            [
                None,
                config["image_iterator_args"]["IMAGE_SIZE"][0],
                config["image_iterator_args"]["IMAGE_SIZE"][1],
                3,
            ]
        )

    def extract_features(self, image_iterator):
        """
        Extracts(if not extracted before) and saves the features of images
        @param image_iterator: image iterator
        @return:normalized features of images
        """

        if "extracted_features.npy" in os.listdir("data"):
            return np.load("data/extracted_features.npy")

        image_features = self.model.predict(image_iterator, verbose=1)
        normalized_features = image_features / np.linalg.norm(
            image_features, ord=2, axis=1, keepdims=True
        )
        np.save("data/extracted_features.npy", normalized_features)
        return normalized_features
