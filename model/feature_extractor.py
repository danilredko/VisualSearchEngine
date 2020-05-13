import os

import tensorflow as tf
import tensorflow_hub as hub
import numpy as np


class FeatureExtractor:

    def __init__(self, hub_model_url, model_build_args):

        self.model = tf.keras.Sequential(
            [
                hub.KerasLayer(
                    "https://tfhub.dev/google/imagenet/mobilenet_v2_050_96/feature_vector/4",
                    trainable=False,
                ),
            ]
        )
        self.model.build([None, 96, 96, 3])

    def extract_features(self, image_iterator):

        if 'extracted_features.npy' in os.listdir('model'):
            return np.load('model/extracted_features.npy')

        image_features = self.model.predict(image_iterator, verbose=1)
        normalized_features = image_features / np.linalg.norm(image_features, ord=2, axis=1, keepdims=True)
        np.save('model/extracted_features', normalized_features)
        return normalized_features



