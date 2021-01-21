<div align="center"><img src="https://github.com/NippunSharma/ChatterBox/blob/main/logo.jpg?raw=true"></div>

<h1 align="center">ChatterBox</h1>

This is a chatbot to answer queries of freshers joining IIT Mandi!

Currently, the bot supports queries of two forms - voice messages and text messages on telegram. For both of these, the bot will send a text message as a response to the query asked by the user.

# Procedure

First, clone this repo by running -
```
git clone https://www.github.com/NippunSharma/ChatterBox
cd ChatterBox
```

Next, install the external dependency `ffmpeg`.<br>
On Ubuntu, you can execute the following -
```
sudo apt update
sudo apt install ffmpeg
```

On Windows, you can do the following -

1. Download the latest version of `ffmpeg` from [here](https://www.gyan.dev/ffmpeg/builds/).
2. Extract the folder to `C:\Program Files\ffmpeg`. (IMPORTANT : If you want to extract it elsewhere, you will have to manually change the path of `ffmpeg` in Line 67 of `telegram_bot.py`).

Once that is done, you have to create a virtual environment and activate it.
```
python -m venv bot
source ./bot/bin/activate
```

Now, you have to run `setup.sh`. This will install the packages from `requirements.txt` and then download packages for `nltk`.
```
chmod +x setup.sh
./setup.sh
```

Create a `.env` file with the following content -
```
TELEGRAM_API_KEY=<your_api_key>
```

Setup is now done! To start chatting with the bot, run `python chatbot.py` and start messaging [@ChatterBoxxBot](https://web.telegram.org/#/im?p=@ChatterBoxxBot) on Telegram.<br>
Have a look at the [Usage Guide](https://github.com/NippunSharma/ChatterBox/blob/main/UsageGuide.pdf) for usage details and various commands.

# Demos

![demo_1](https://github.com/NippunSharma/ChatterBox/blob/main/demo/ChatterBox_1.png)
![demo_2](https://github.com/NippunSharma/ChatterBox/blob/main/demo/ChatterBox_2.png)
![demo_3](https://github.com/NippunSharma/ChatterBox/blob/main/demo/ChatterBox_3.png)