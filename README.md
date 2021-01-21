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
3. Add this folder to the path using the following command in Powershell -
```
setx /m PATH "<path to ffmpeg>/bin;%PATH%"
```

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
