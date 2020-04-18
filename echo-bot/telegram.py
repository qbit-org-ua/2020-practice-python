# https://github.com/eternnoir/pyTelegramBotAPI
#
# pip install pyTelegramBotAPI

import telebot

with open("telegram-bot-token.txt") as bot_key_file:
    BOT_TOKEN = bot_key_file.read().strip()

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(content_types=["sticker"])
def echo_sticker(message):
    bot.reply_to(message, "стикер!")
    bot.send_sticker(
        message.chat.id,
        # "CAACAgIAAxkBAAOJXpr3cZxLHRO9qqjxKrP2MhOz8PkAAnsFAAIYQu4IC-aeYd6A0wMYBA",
        message.sticker.file_id,
    )


@bot.message_handler()
def echo(message):
    # print(message)
    if message.text.lower() == "hi":
        bot.reply_to(message, "Hi!")
    else:
        bot.send_message(message.chat.id, f"Hello, {message.from_user.first_name}")
    bot.delete_message(message.chat.id, message.message_id)


bot.polling()
