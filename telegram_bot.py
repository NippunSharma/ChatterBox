import requests
import json
import subprocess
import speech_recognition as sr
import sys
import os
from dotenv import load_dotenv

#Load .env file containing API_KEY
load_dotenv(dotenv_path='.env')
# API Key of the bot.
TOKEN = os.environ['TELEGRAM_API_KEY']


def speech2text(audio_file):
    '''
    This function take as input the name of an audio file and 
    converts it into text string.
    '''
    r = sr.Recognizer()
    query = sr.AudioFile(audio_file)
    with query as source:
        audio = r.record(source)

    if sys.platform == "linux":
        subprocess.run(['rm', audio_file])
    else:
        subprocess.run('del /f -y ' + audio_file, shell=True)
    try:
        print('Recognising....')
        text = r.recognize_google(audio)
        # print('User said: ', text)
    except Exception as e:
        print("Could not understand")
        return None

    return text


class TelegramChatbot():
    def __init__(self):
        self.token = TOKEN
        self.base = f"https://api.telegram.org/bot{self.token}"

    def getUpdates(self, offset=None):
        url = self.base + "/getUpdates?timeout=100"
        if offset:
            url = url + f"&offset={offset + 1}"
        r = requests.get(url)
        return json.loads(r.content)

    def sendMessage(self, message, chat_id):
        url = self.base + f"/sendMessage?chat_id={chat_id}&text={message}"
        if message is not None:
            requests.get(url)

    def _getFilePath(self, file_id):
        url = self.base + f"/getFile?file_id={file_id}"
        r = requests.get(url)
        updates = json.loads(r.content)
        file_path = updates["result"]["file_path"]
        return file_path

    def downloadFile(self, file_id):
        file_path = self._getFilePath(file_id)
        with open("temp", "wb") as file:
            url = f"https://api.telegram.org/file/bot{self.token}" + \
                "/" + file_path
            r = requests.get(url)
            file.write(r.content)
        if sys.platform == 'linux':
            convert = subprocess.run(['ffmpeg', '-i', "temp", "query.wav"])
            subprocess.run(['rm', 'temp'])
        else:
            convert = subprocess.run('"C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe" -i temp query.wav')
            subprocess.run('del /f -y temp', shell=True)
        if convert.returncode != 0:
            raise Exception("Something went wrong")
