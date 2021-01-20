"""Main program"""

from pywsd.utils import lemmatize_sentence
from searchData import search
from matchData import match
from numpy.random import choice
from googleSearch import google_search
import json
import time
import requests

from weather import currentWeather

with open("data/talk.json", "rb") as file:
    greetDic = json.load(file)
file.close()


def greet(inpText):
    """This function creates a greeting
    based on the input if required."""
    global greetDic

    flag = False
    for key in greetDic.keys():
        if " ".join(process(key)) in " ".join(process(inpText)):
            randGreet = choice(greetDic[key], size=1)[0]
            flag = True
            print(randGreet)
    return flag


def process(inpText):
    """This function lemmatizes
    the input sentence."""
    l = lemmatize_sentence(inpText, keepWordPOS=True)
    return l[1]


# Writing main loop.
mainFlag = True
while(mainFlag):
    # obtaining the input.
    inputMsg = input("> ").strip(" ")

    # loop terminating condition.
    # if inputMsg.lower() == "end":
    #     print("Happy to be of assistance!!")
    #     mainFlag = False
    # else:

    # processing input message.
    # checking if message is related to coding
    # or not.
    if inputMsg.split()[0] == "!code":
        # print("Searching for possible answers..")
        # time.sleep(2)
        print("Plese refer to the following link: ")
        google_search(" ".join(inputMsg.split(" ")[1:]))
    elif inputMsg.split()[0] == "!faq":
        print("Searching....")
        ansMatch = match(inputMsg, "data/final_concat.csv")
        print(ansMatch)
    elif inputMsg.split()[0] == "!weather":
        try:
            city = " ".join(inputMsg[1:])
            print(currentWeather(city))
        except Exception as e:
            print("Type a valid city name.")
    else:
        processedMsg = process(inputMsg)
        # greeting if needed.
        greetFlag = greet(inputMsg)
        # getting data to create an answer.
        ans, altans1 = search(processedMsg, "data/abtCollege.json")

        altans = dict()
        for key in altans1:
            altans[key.lower()] = altans1[key]

        ans = "".join(list(ans))

        # handling if only greet is present inside input.
        if (ans == "" and greetFlag):
            continue
        elif (ans == "" and not greetFlag):
            print("Answer not found in main database...")
            print(
                "Do you want me to search in the Facebook groups of previous year and other sites like Quora ?")
            faq = input("> ").strip().lower()
            if "yes" in faq or "yup" in faq:
                print("Searching ....")
                ansMatch = match(inputMsg, "data/final_concat.csv")
                print(ansMatch)
            else:
                print("Okay.")
        else:
            print(ans)
            randAltAns = choice(list(altans1.keys()),
                                size=2, replace=False)
            if len(altans) != 0:
                QUES = "Do you wish to know more about "
                # alternate answers
                print(QUES + ", ".join(randAltAns) + "?")
                altInpMsg = input("> ").strip().lower()
            if ("yes" in altInpMsg):
                string = ""
                if len(altans) != 0:
                    for w in randAltAns:
                        if w in altInpMsg:
                            string += altans1[w] + "\n"
                    if string != "":
                        print("Okay! Here you go.")
                        print(string)
                    else:
                        print("Can you repeat your question ?")
                    #processedAltAns = process(altInpMsg)
                    #ans, _  = search(processedAltAns, "data/abtCollege.json")
                    #ans = "".join(list(ans))
                    # if ans == "":
                    #    print("".join(list(altans.values())))
                    # else:
                    #    print(ans)
            elif ("no" in altInpMsg):
                print("Your choice.. I was just trying to help.")
            else:
                processedAltAns = process(altInpMsg)
                ans, _ = search(processedAltAns, "data/abtCollege.json")
                ans = "".join(list(ans))
                if ans == "":
                    print("I can't help you :(")
                else:
                    print(ans)
                #print("Can you repeat what you just said ?")
