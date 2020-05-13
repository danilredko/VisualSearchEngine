from model.feature_extractor import FeatureExtractor
from model.data_loader import ImageIterator
from model.feature_storage import FeatureStorage
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

iterator = ImageIterator((96, 96), 32).directory_iterator
image_features = FeatureExtractor.load_features()
storage = FeatureStorage(image_features, iterator)

I = storage.get_top_k_similar('10004.jpg', 4)
fig, axs = plt.subplots(1, 4)

file_names = iterator.filenames
for i, idx in enumerate(I):
    img = mpimg.imread(f'../dataset/{file_names[idx]}')
    axs[i].imshow(img)
    axs[i].axis('off')
plt.show()





