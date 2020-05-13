import faiss
import time
import numpy as np


class FeatureStorage:

    def __init__(self, image_features, iterator):

        self.iterator = iterator
        self.image_features = image_features
        self.index = faiss.IndexFlatIP(image_features.shape[1])
        self.index.add(image_features)

    def get_top_k_similar(self, image_name, top_k):

        file_names = self.iterator.filenames
        im_index = file_names.index(f'images/{image_name}')
        im_feature = np.array([self.image_features[im_index]])
        D, I = self.index.search(im_feature, top_k)

        return I[0]

        # fig, axs = plt.subplots(4, 1)
        # for i, idx in enumerate(I[0]):
        #     print(filenames[idx])
        #     img = mpimg.imread(f'dataset/{filenames[idx]}')
        #     axs[i].imshow(img)
        # plt.show()
        #
        # find_closest_images("10000.jpg", k)
