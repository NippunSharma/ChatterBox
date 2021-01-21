# ChatterBox

Currently the bot supports queries in two forms - voice messages and text messages on telegram. For both of these, the bot will send a text message as a response to the query asked by the user.

# Procedure

First, install the external dependency `ffmpeg`.<br>
On Ubuntu, you can use -
```
sudo apt update
sudo apt install ffmpeg
```

On Windows, you can do the following -

1. Download the latest version of `ffmpeg` from the [here](https://www.gyan.dev/ffmpeg/builds/).
2. Extract the folder to `C:\Program Files\ffmpeg`. (IMPORTANT : If you want to extract it elsewhere, you will have to manually change the path of ffmpeg in Line 67 of `telegram_bot.py`).

Next, you have to create a virtual environment and activate it.
```
python -m venv bot
source ./bot/bin/activate
```

Now, you have to run `setup.sh`. This will install the packages from `requirements.txt` and then download packages for `nltk`.
```
chmod +x setup.sh
./setup.sh
```

Setup is now done! To start chatting with the bot, run `python chatbot.py`.
Have a look at the [Usage Guide](https://github.com/NippunSharma/ChatterBox/blob/main/doc.pdf) for usage details and various commands.

Note: Sometimes, due to problems in loops, the bot may not give an answer to a question the first time you ask it. It is suggested that you try asking the question again. You might get the correct answer this time. If the bot still is not able to find the answer, then the answer cannot be found by the bot.
