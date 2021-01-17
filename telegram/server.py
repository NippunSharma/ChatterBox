from bot import TelegramChatbot, speech2text
from time import sleep


update_id = None
bot = TelegramChatbot()

while True:
    print(".......")
    updates = bot.getUpdates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            message = item["message"]
            from_ = message["chat"]["id"]

    text, voice = (None, None)
    try:
        text = message["text"]
        bot.sendMessage(text, from_)
    except:
        pass
    try:
        file_id = message["voice"]["file_id"]
        bot.downloadFile(file_id)
        bot.sendMessage(speech2text('query.wav'), from_)

    except:
        pass

    sleep(1)
