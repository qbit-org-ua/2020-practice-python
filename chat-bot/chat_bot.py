# -*- coding: utf-8 -*-
"""
This Example will show you how to use register_next_step handler.
"""
import json

import telebot
from telebot import types

with open("telegram-api-token.txt") as token_file:
    TELEGRAM_TOKEN = token_file.read().strip()

bot = telebot.TeleBot(TELEGRAM_TOKEN)

user_dict = {}


class User:
    def __init__(self, name):
        self.name = name
        self.age = None
        self.sex = None

    def __repr__(self):
        return f"User({self.name}, {self.age}, {self.sex})"


def save_users():
    dumped_users = {}
    for chat_id, user in user_dict.items():
        dumped_users[chat_id] = {
            "name": user.name,
            "age": user.age,
            "sex": user.sex,
        }
    with open("users.json", "w") as users_file:
        users_file.write(json.dumps(dumped_users, indent=2))


def load_users():
    with open("users.json") as users_file:
        loaded_users = json.loads(users_file.read())
    for chat_id, user_as_dict in loaded_users.items():
        user = User(user_as_dict["name"])
        user.age = user_as_dict["age"]
        user.sex = user_as_dict["sex"]
        user_dict[int(chat_id)] = user


try:
    load_users()
except:
    print("Не смог загрузить пользователей")

# Handle '/start' and '/help'
@bot.message_handler(commands=["help", "start"])
def send_welcome(message):
    msg = bot.reply_to(
        message,
        """\
Hi there, I am Example bot.
What's your name?
""",
    )
    bot.register_next_step_handler(msg, process_name_step)


def process_name_step(message):
    chat_id = message.chat.id
    name = message.text
    user = User(name)
    user_dict[chat_id] = user
    try:
        msg = bot.reply_to(message, "How old are you?")
        bot.register_next_step_handler(msg, process_age_step)
    except Exception as e:
        bot.reply_to(message, "oooops")


def process_age_step(message):
    chat_id = message.chat.id
    age = message.text
    try:
        if not age.isdigit():
            msg = bot.reply_to(message, "Age should be a number. How old are you?")
            bot.register_next_step_handler(msg, process_age_step)
            return
        user = user_dict[chat_id]
        user.age = age
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add("Male", "Female")
        msg = bot.reply_to(message, "What is your gender", reply_markup=markup)
        bot.register_next_step_handler(msg, process_sex_step)
    except Exception as e:
        bot.reply_to(message, "oooops")


def process_sex_step(message):
    print(user_dict)
    chat_id = message.chat.id
    sex = message.text
    try:
        user = user_dict[chat_id]
        if sex == "Male" or sex == "Female":
            user.sex = sex
        else:
            raise Exception()

        save_users()

        bot.send_message(
            chat_id, f"Nice to meet you {user.name}\n Age: {user.age}\n Sex: {user.sex}"
        )
    except Exception as e:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add("Male2", "Female2")
        msg = bot.reply_to(message, "What is your gender", reply_markup=markup)
        bot.register_next_step_handler(msg, process_sex_step)


@bot.message_handler(commands=["about_me"])
def about_me(message):
    user = user_dict.get(message.chat.id)
    if user is None:
        bot.send_message(message.chat.id, "Нет информации")
    else:
        print(user)
        bot.send_message(
            message.chat.id, f"You are {user.name}\n Age: {user.age}\n Sex: {user.sex}"
        )


@bot.message_handler(commands=["all_users"])
def all_users(message):
    for user in list(user_dict.values()):
        bot.send_message(
            message.chat.id, f"User {user.name}\n Age: {user.age}\n Sex: {user.sex}"
        )


@bot.message_handler()
def broadcast(message):
    user = user_dict.get(message.chat.id)
    if user is None:
        bot.send_message(message.chat.id, "Заполните профиль: /start")
        return

    for chat_id in list(user_dict.keys()):
        if message.chat.id == chat_id:
            continue
        bot.send_message(chat_id, f"{user.name}: {message.text}")


# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()

bot.polling()
