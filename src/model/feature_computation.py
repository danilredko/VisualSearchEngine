import pickle

import faiss

from model.feature_extractor import FeatureExtractor
from model.image_iterator import ImageIterator
from model.config import Config


class FeatureComputer:
    def __init__(self, model_name):
        self.config = Config().config
        self.iterator = ImageIterator(self.config[model_name]).directory_iterator
        self.image_features = FeatureExtractor(
            self.config[model_name]
        ).extract_features(self.iterator)

    def save_filenames(self):
        filenames = self.iterator.filenames
        with open('data/filenames.pickle', 'wb') as handle:
            pickle.dump(filenames, handle)
