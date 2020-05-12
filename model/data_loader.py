import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import faiss

import time

import matplotlib.image as mpimg
import matplotlib.pyplot as plt

num_classes = 10

IMAGE_SIZE = (96, 96)
BATCH_SIZE = 32

datagen = tf.keras.preprocessing.image.ImageDataGenerator(
    rotation_range=40,
    horizontal_flip=True,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    rescale=1.0 / 255,
)

directory_iterator = tf.keras.preprocessing.image.DirectoryIterator(
    "dataset",
    datagen,
    target_size=IMAGE_SIZE,
    color_mode="rgb",
    classes=None,
    batch_size=BATCH_SIZE,
    shuffle=False,
    seed=9,
)

m = tf.keras.Sequential(
    [
        hub.KerasLayer(
            "https://tfhub.dev/google/imagenet/mobilenet_v2_050_96/feature_vector/4 (https://tfhub.dev/google/imagenet/mobilenet_v2_050_96/feature_vector/4)",
            trainable=False,
        ),
    ]
)
m.build([None, 96, 96, 3])

image_features = m.predict(directory_iterator, verbose=1)
normalized_im = image_features/np.linalg.norm(image_features, ord=2, axis=1, keepdims=True)

d = 1280

index = faiss.IndexFlatIP(d)
t = time.time()
index.add(image_features)
print(time.time() - t)

k = 4

filenames = directory_iterator.filenames

def find_closest_images(im_name, k):
    im_index = filenames.index(f'images/{im_name}')
    im_feature = np.array([image_features[im_index]])
    t = time.time()
    D, I = index.search(im_feature, k)
    print(time.time() - t)

    fig, axs = plt.subplots(4, 1)
    for i, idx in enumerate(I[0]):
        print(filenames[idx])
        img = mpimg.imread(f'dataset/{filenames[idx]}')
        axs[i].imshow(img)
    plt.show()

find_closest_images("10000.jpg", k)