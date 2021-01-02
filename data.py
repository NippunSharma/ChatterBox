# This file contains all the data preprocessing tasks.
import json
import numpy as np
import pickle

data = None
with open("intents.json") as file:
    data = json.load(file)
file.close()

data = dict(data)

labels = [x["tag"] for x in data["intents"] for _ in range(len(x["patterns"]))]
training_sentences = [y for x in data["intents"] for y in x["patterns"]]

with open("yTrain.pickle", "wb") as file:
    pickle.dump(labels, file)
file.close()

with open("xTrain.pickle", "wb") as file:
    pickle.dump(training_sentences, file)
file.close()
