import tensorflow as tf
import numpy as np
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout
from keras.utils.image_dataset import image_dataset_from_directory

in_folder = 118
size = 256
data_dir = "./AI_train"

train_dataset = image_dataset_from_directory(
    data_dir + "/train",  # от наличия /tarin или /val ошибка не меняется
    labels="inferred",
    label_mode='categorical',
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