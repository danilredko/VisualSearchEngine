from model.feature_extractor import FeatureExtractor
from model.data_loader import ImageIterator
from model.feature_storage import FeatureStorage
from model.config import Config
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


class VisualSearch:

    def __init__(self):

        self.config = Config().config
        self.iterator = ImageIterator(tuple(self.config['image_generator_args']['IMAGE_SIZE']), self.config['image_generator_args']['BATCH_SIZE']).directory_iterator
        self.image_features = FeatureExtractor("dsfasdf", "asdfas").extract_features(self.iterator)
        self.storage = FeatureStorage(self.image_features)

    def show_top_k(self, image_name, top_k):

        file_names = self.iterator.filenames
        I = self.storage.get_top_k_similar(image_name, file_names, top_k)
        fig, axs = plt.subplots(1, top_k)

        for i, idx in enumerate(I):
            img = mpimg.imread(f'dataset/{file_names[idx]}')
            axs[i].imshow(img)
            axs[i].axis('off')
        plt.show()





