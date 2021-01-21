"""Main program"""

from pywsd.utils import lemmatize_sentence
from searchData import search
from matchData import match
from numpy.random import choice
from googleSearch import google_search
import json
import requests

from telegram_bot import TelegramChatbot, speech2text
from time import sleep

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
            bot.sendMessage(randGreet, from_)
    return flag


def process(inpText):
    """This function lemmatizes
    the input sentence."""
    l = lemmatize_sentence(inpText, keepWordPOS=True)
    return l[1]

update_id = None
bot = TelegramChatbot()

def getMessage(update_id, from_ = None):
    # updates contains all the details about the latest message sent by user.
    updates = bot.getUpdates(offset=update_id)
    updates = updates["result"]

    # Extracting required fields from updates.
    
    if updates:
        for item in updates:
            # It helps us to fetch the latest message instead of the whole chat history.
            update_id = item["update_id"]
            # Contains all the details of the message.
            try:
                message = item["message"]
            except:
                message = item["edited_message"]
            from_ = message["chat"]["id"]   # chat_id of the user.

        # text ---> text query from user.
    # voice ---> voice message from user.
    inputMsg = ""

    # Handling the text input from user.
    try:
        inputMsg = message["text"].strip(" ")
    except:
        pass

    # Handling voice input from user.
    try:
        file_id = message["voice"]["file_id"]
        bot.downloadFile(file_id)
        inputMsg = speech2text('query.wav').strip(" ")
        print("User said:", inputMsg)
    except:
        pass

    return inputMsg, update_id, from_


# Writing main loop.
mainFlag = True
while(mainFlag):
    print("........")
    # obtaining the input.
    inputMsg, update_id, from_ = getMessage(update_id, from_ = None)
    inputMsg = inputMsg.strip()

    command = ""

    try:
        command = inputMsg.split()[0]
    except:
        pass

    # checking if message is related to coding
    # or not.
    if command == "/start":
        bot.sendMessage("Hi! Glad to know that you've chosen to take my help! What can I assist you with ?", from_)
    elif command == "!code":
        bot.sendMessage("Plese refer to the following link: ", from_)
        bot.sendMessage(google_search(" ".join(inputMsg.split(" ")[1:])), from_)
    elif command == "!faq":
        ansMatch = match(inputMsg, "data/final_concat.csv")
        bot.sendMessage(ansMatch, from_)
    elif command == "!weather":
        try:
            city = " ".join(inputMsg.split()[1:])
            bot.sendMessage(currentWeather(city), from_)
        except Exception as e:
            bot.sendMessage("Unable to process the request.", from_)
    else:
        processedMsg = process(inputMsg)
        # greeting if needed.
        greetFlag = greet(inputMsg)
        # getting data to create an answer.
        ans, altans1 = search(processedMsg, "data/abtCollege.json")

        altans = dict()
        for key in altans1:
            altans[key.lower()] = altans1[key]

        ans = "\n".join(list(ans))

        # handling if only greet is present inside input.
        if (ans == "" and greetFlag):
            continue
        elif (ans == "" and not greetFlag):
            bot.sendMessage("Answer not found in main database...", from_)
            bot.sendMessage("Do you want me to search in the Facebook groups of previous year and other sites like Quora ?", from_)
            faq, update_id, from_ = getMessage(update_id, from_)
            faq = faq.strip().lower()
            if "yes" in faq or "yup" in faq:
                ansMatch = match(inputMsg, "data/final_concat.csv")
                bot.sendMessage(ansMatch, from_)
            elif "no" in faq:
                bot.sendMessage(
                    "Your choice.. I was just trying to help.", from_)
            else:
                bot.sendMessage("Sorry, I am unable to answer that. Please ask me something else :)", from_)
        else:
            bot.sendMessage(ans, from_)
            randAltAns = choice(list(altans.keys()),
                                size=2, replace=False)
            if len(altans) != 0:
                QUES = "Do you wish to know more about "
                # alternate answers
                bot.sendMessage(QUES + ", ".join(randAltAns) + "?", from_)
                altInpMsg, update_id, from_ = getMessage(update_id, from_)
                altInpMsg = altInpMsg.strip().lower()
            if ("yes" in altInpMsg):
                string = ""
                if len(altans1) != 0:
                    for w in randAltAns:
                        if w in altInpMsg:
                            string += altans[w] + "\n"
                    if string == "":
                        for w in randAltAns:
                            string += altans[w] + "\n"
                    if string != "":
                        bot.sendMessage("Okay! Here you go.", from_)
                        bot.sendMessage(string, from_)
            elif ("no" in altInpMsg):
                bot.sendMessage(
                    "Your choice.. I was just trying to help.", from_)
            else:
                #processedAltAns = process(altInpMsg)
                #ans, _ = search(processedAltAns, "data/abtCollege.json")
                #ans = "".join(list(ans))
                #if ans == "":
                    #bot.sendMessage("I can't help you :(", from_)
                #else:
                    #bot.sendMessage(ans, from_)
                bot.sendMessage(
                    "I cannot find what you are looking for :(", from_)
