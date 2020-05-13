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

    def extract(self, image_iterator):

        image_features = self.model.predict(image_iterator, verbose=1)
        return image_features

    def save_features(self, image_iterator):

        image_features = self.extract(image_iterator)
        np.save('extracted_features', image_features)
        return image_features

    @staticmethod
    def load_features():
        return np.load('extracted_features.npy')




