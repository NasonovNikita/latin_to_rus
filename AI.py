import os
import tensorflow as tf
import numpy as np
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout
from keras.utils.image_dataset import image_dataset_from_directory

in_folder = 118
size = 256
data_dir = "./AI_train"
cnt = len(os.listdir(data_dir))

train_ds = image_dataset_from_directory(
    data_dir + "/train",
    seed=2,
    image_size=(size, size),
    batch_size=in_folder
)

val_ds = tf.keras.utils.image_dataset_from_directory(
    data_dir + '/val',
    labels="inferred",
    label_mode='categorical',
    seed=2,
    image_size=(size, size),
    batch_size=in_folder)

normalization_layer = tf.keras.layers.Rescaling(1./255)

model = keras.Sequential([
    normalization_layer,
    keras.layers.Flatten(input_shape=(size, size)),
    keras.layers.Dense(2048, activation="relu")
])

model.compile(loss='sparse_categorical_crossentropy', metrics=["accuracy"])

model.fit(train_ds, epochs=10)