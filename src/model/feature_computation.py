import pickle

import faiss

from model.feature_extractor import FeatureExtractor
from model.image_iterator import ImageIterator
from model.config import Config


class FeatureComputer:
    """
    A class to represent Feature Computer

    ...

    Attributes
    __________
    config:
        contains all necessary parameters for Image Iterator and Feature Extractor
    iterator:
        image iterator, refect to Image Iterator Doc
    image_features:
        image features extracted by Feature Extractor
    """

    def __init__(self, model_name):
        """
        Constructs all the necessary attributes for Feature Computer Object
        @param model_name: name of a model to use(defined in config.json)
        """
        self.config = Config().config
        self.iterator = ImageIterator(self.config[model_name]).directory_iterator
        self.image_features = FeatureExtractor(
            self.config[model_name]
        ).extract_features(self.iterator)

    def save_filenames(self):
        """Saves the filenames object to pickle file"""

        filenames = self.iterator.filenames
        with open('data/filenames.pickle', 'wb') as handle:
            pickle.dump(filenames, handle)
