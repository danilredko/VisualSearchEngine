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

        image_features = self.model.predict(image_iterator, verbose=1)
        normalized_features = image_features / np.linalg.norm(image_features, ord=2, axis=1, keepdims=True)
        return normalized_features

    def save_features(self, image_iterator):

        normalized_features = self.extract_features(image_iterator)
        np.save('extracted_features', normalized_features)
        return normalized_features

    @staticmethod
    def load_features():

        return np.load('extracted_features.npy')


