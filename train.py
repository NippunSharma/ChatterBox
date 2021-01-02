# This file contains model creation and training.
import numpy as np
import tensorflow as tf
from data import VOCAB_SIZE, EMBEDDING_DIM, MAX_LEN, NUM_CLASSES

xTrain = np.load("xTrain.npz")
xTrain = xTrain["arr_0"]

yTrain = np.load("yTrain.npz")
yTrain = yTrain["arr_0"]

xTrain = tf.convert_to_tensor(xTrain)
yTrain = tf.convert_to_tensor(yTrain)

tf.keras.backend.clear_session()

inp = tf.keras.Input(shape=(xTrain.shape[1],))
x = tf.keras.layers.Embedding(input_dim=VOCAB_SIZE, output_dim=EMBEDDING_DIM, input_length=MAX_LEN)(inp)
x = tf.keras.layers.GlobalAveragePooling1D()(x)
x = tf.keras.layers.Dense(16, activation="relu")(x)
out = tf.keras.layers.Dense(NUM_CLASSES, activation="softmax")(x)

model = tf.keras.models.Model(inputs=inp, outputs=out)
model.compile(loss="categorical_crossentropy", optimizer=tf.keras.optimizers.Adam())
model.fit(xTrain, yTrain, epochs=10)

model.save("bot_core")
