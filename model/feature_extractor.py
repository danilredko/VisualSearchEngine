import os

import tensorflow as tf
import tensorflow_hub as hub
import numpy as np


class FeatureExtractor:
    def __init__(self, config):
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

        if "extracted_features.npy" in os.listdir("model"):
            return np.load("model/extracted_features.npy")

        image_features = self.model.predict(image_iterator, verbose=1)
        normalized_features = image_features / np.linalg.norm(
            image_features, ord=2, axis=1, keepdims=True
        )
        np.save("model/extracted_features.npy", normalized_features)
        return normalized_features
