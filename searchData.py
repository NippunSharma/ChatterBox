"""Searching in JSON file"""

import json
from pywsd.utils import lemmatize_sentence

courses = ['resp0nse', 'DP', 'RM', 'CE', 'HS', 'CS', 'EM', 'XX', 'EN', 'BY', 'Mechanical', 'MA', 'PH', 'EE', 'IC', 'CY']

def search(keywords, filename):
    f = open(filename, 'r')

    data = json.loads(f.read())
    f.close()

    def recurse(key, d, ans, altans):
        key_lem = None
        if key in courses:
            key_lem = key.lower().strip()
        else:
            key_lem = lemmatize_sentence(key)[0]
        #print("Lemmatized key: " + key_lem)
        #print("Original Key: " + key)
        if key_lem in keywords:
            ans.add(d[key]['resp0nse'])
            for j in d:
                if j != key and j != 'resp0nse':
                    #try:
                    #   altans[j] += d[j]['resp0nse']
                    #except:
                    altans.update({j : d[j]['resp0nse']})
        if type(d[key]) == dict:
            for i in d[key]:
                if i != 'resp0nse':
                    ans, altans = recurse(i, d[key], ans, altans)
        return ans, altans

    a, b = recurse("st3rt", data, set(), dict())
    for i in keywords:
        if i in b:
            del b[i]
    return a, b