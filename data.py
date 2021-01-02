# This file contains all the data preprocessing tasks.
import json
import numpy as np
import pickle
from sklearn.preprocessing import OneHotEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

data = None
with open("intents.json") as file:
    data = json.load(file)
file.close()

data = dict(data)

labels = [x["tag"] for x in data["intents"] for _ in range(len(x["patterns"]))]
training_sentences = [y for x in data["intents"] for y in x["patterns"]]

encode = OneHotEncoder()
labels_ohe = encode.fit_transform(np.array(labels).reshape(-1,1)).toarray()

VOCAB_SIZE = 1000
EMBEDDING_DIM = 16
MAX_LEN = 20
OOV_TOKEN = "<OOV>"

tokenizer = Tokenizer(num_words=VOCAB_SIZE, oov_token=OOV_TOKEN)
tokenizer.fit_on_texts(training_sentences)

WORD_INDEX = tokenizer.word_index
sequences = tokenizer.texts_to_sequences(training_sentences)

padded_sequences = np.array(pad_sequences(sequences, truncating='post', maxlen=MAX_LEN, padding="post"))

np.savez_compressed("xTrain.npz", padded_sequences)
np.savez_compressed("yTrain.npz", labels_ohe)
