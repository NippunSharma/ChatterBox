from pywsd.utils import lemmatize_sentence
import pandas as pd

def match(inp, filename):
    exclude = ["iit", "mandi", "!", "?", "-", ".", ",", "in", "at",
                "on"]

    for i in exclude:
        inp = inp.replace(i, "")

    data = pd.read_csv(filename)
    processedInp = lemmatize_sentence(inp.strip().lower())

    maxSim = -1
    ans = None
    bestQues = None
    for idx in range(data.shape[0]):
        processedQues = lemmatize_sentence(data.question[idx].strip().lower())
        sim = len(set(processedInp).intersection(set(processedQues)))
        if sim > maxSim:
            maxSim = sim
            bestQues = data.question[idx]
            ans = data.answers[idx]
    if maxSim == 0:
        return "Sorry, I cannot answer you... Some secrets are best not to be revealed :)"
    else:
        print("Your question matched to the following question in database...")
        print(bestQues)
        print("Answer: ")
        return ans