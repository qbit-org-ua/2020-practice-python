from datetime import datetime
import threading
import time

import telebot

with open("telegram-api-token.txt") as token_file:
    TELEGRAM_TOKEN = token_file.read().strip()

bot_qq = telebot.TeleBot(TELEGRAM_TOKEN)

START_DATE = datetime(2020, 5, 10)
count_downs = {}


def format_announcement():
    till = START_DATE - datetime.now()
    return f"KhCup начнётся {START_DATE}, через {till}"


@bot_qq.message_handler(commands=["start"])
def start(message):
    msg = bot_qq.send_message(message.chat.id, format_announcement())
    count_downs[message.chat.id] = msg.message_id


def update_count_downs():
    while True:
        for chat_id, message_id in count_downs.items():
            bot_qq.edit_message_text(format_announcement(), chat_id, message_id)
        time.sleep(1)


threading.Thread(target=update_count_downs).start()

bot_qq.polling()

print("Bye.")
