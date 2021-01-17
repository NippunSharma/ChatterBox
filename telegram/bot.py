import requests
import json
import subprocess
import speech_recognition as sr

TOKEN = "1521698483:AAHTyz_22-Q48iYVU6NC5ynWMUhoPC6QREA"


def speech2text(audio_file):
    r = sr.Recognizer()
    query = sr.AudioFile(audio_file)
    with query as source:
        audio = r.record(source)

    subprocess.run(['rm', audio_file])
    try:
        print('Recognising....')
        text = r.recognize_google(audio)
        print('User said: ', text)
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
        convert = subprocess.run(
            ['ffmpeg', '-i', "temp", "query.wav"])
        subprocess.run(['rm', 'temp'])

        if convert.returncode != 0:
            raise Exception("Something went wrong")
