from model.feature_extractor import FeatureExtractor
from model.data_loader import ImageIterator
from model.feature_storage import FeatureStorage
from model.config import Config
from model.score_calculation import ScoreCalculator
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


class VisualSearch:

    def __init__(self, model_name):

        self.config = Config().config
        self.iterator = ImageIterator(self.config[model_name]).directory_iterator
        self.image_features = FeatureExtractor(self.config[model_name]).extract_features(self.iterator)
        self.storage = FeatureStorage(self.image_features)
        self.score_calc = ScoreCalculator()

    def show_top_k(self, image_name, top_k):

        file_names = self.iterator.filenames
        I = self.storage.get_top_k_similar(image_name, file_names, top_k)
        fig, axs = plt.subplots(2, top_k)
        fig(figsize=(10, 10))

        for i, idx in enumerate(I):

            img = mpimg.imread(f'dataset/{file_names[idx]}')
            axs[i].imshow(img)
            axs[i].set_title('Similarity: '+str(self.score_calc.calculate_precision(image_name, file_names[idx])))
            axs[i].axis('off')

        plt.title('Top {} similar images'.format(top_k))
        plt.show()





