from bot import TelegramChatbot, speech2text
from time import sleep


update_id = None
bot = TelegramChatbot()

while True:
    print(".......")
    # updates contains all the details about the latest message sent by user.
    updates = bot.getUpdates(offset=update_id)
    updates = updates["result"]

    # Extracting required fields from updates.
    if updates:
        for item in updates:
            # It helps us to fetch the latest message instead of the whole chat history.
            update_id = item["update_id"]
            # Contains all the details of the message.
            message = item["message"]
            from_ = message["chat"]["id"]   # chat_id of the user.

    # text ---> text query from user.
    # voice ---> voice message from user.
    text, voice = (None, None)

    # Handling the text input from user.
    try:
        text = message["text"]
        # Currently bot sends the same text as typed by user.
        # Needs to be updated.
        response = ""
        bot.sendMessage(response, from_)
    except:
        pass

    # Handling voice input from user.
    try:
        file_id = message["voice"]["file_id"]
        bot.downloadFile(file_id)
        # Currently bot sends the same text as typed by user.
        # Needs to be updated.
        bot.sendMessage(speech2text('query.wav'), from_)
    except:
        pass

    sleep(1)
