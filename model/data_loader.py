import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import faiss

import time

import matplotlib.image as mpimg
import matplotlib.pyplot as plt

IMAGE_SIZE = (96, 96)
BATCH_SIZE = 32


class ImageIterator:

    def __init__(self, IMAGE_SIZE, BATCH_SIZE):

        self.datagen = tf.keras.preprocessing.image.ImageDataGenerator(

            rotation_range=40,
            horizontal_flip=True,
            width_shift_range=0.2,
            height_shift_range=0.2,
            shear_range=0.2,
            zoom_range=0.2,
            rescale=1.0 / 255)

        self.directory_iterator = tf.keras.preprocessing.image.DirectoryIterator(
                "../dataset",
                self.datagen,
                target_size=IMAGE_SIZE,
                color_mode="rgb",
                classes=None,
                batch_size=BATCH_SIZE,
                shuffle=False,
                seed=9,
            )





