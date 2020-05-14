import tensorflow as tf


class ImageIterator:
    """
    A class to represent image iterator

    ...

    Attributes
    __________
    datagen:
        image generator used to rescale and modify the images(scale, zoom, etc.)
    directory_iterator:
        iterates on the image directory using the image generator
    """
    def __init__(self, config):

        img_gen_conf = config["image_generator_args"]
        dir_iter_conf = config["image_iterator_args"]
        self.datagen = tf.keras.preprocessing.image.ImageDataGenerator(
            rotation_range=img_gen_conf["rotation_range"],
            horizontal_flip=bool(img_gen_conf["horizontal_flip"]),
            width_shift_range=img_gen_conf["width_shift_range"],
            height_shift_range=img_gen_conf["height_shift_range"],
            shear_range=img_gen_conf["shear_range"],
            zoom_range=img_gen_conf["zoom_range"],
            rescale=1.0 / 255,
        )

        self.directory_iterator = tf.keras.preprocessing.image.DirectoryIterator(
            "dataset",
            self.datagen,
            target_size=tuple(dir_iter_conf["IMAGE_SIZE"]),
            color_mode="rgb",
            classes=None,
            batch_size=dir_iter_conf["BATCH_SIZE"],
            shuffle=False,
            seed=9,
        )
