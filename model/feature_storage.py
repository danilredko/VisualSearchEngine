import faiss
import numpy as np


class FeatureStorage:

    def __init__(self, image_features):

        self.image_features = image_features
        self.index = faiss.IndexFlatIP(image_features.shape[1])
        self.index.add(image_features)

    def get_top_k_similar(self, image_name, file_names, top_k):

        im_index = file_names.index(f'images/{image_name}')
        im_feature = np.array([self.image_features[im_index]])
        D, I = self.index.search(im_feature, top_k)

        return I[0]
