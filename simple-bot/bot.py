"""
MESSAGE = {
    "text": "/add 1 2",
    "cmd_args": "1 2",
    "from_user": {
        "username": "Vlad",
    },
    # ...
}
"""


class User:
    def __init__(self, username):
        self.username = username


class Message:
    def __init__(self, text, cmd_args, from_user):
        self.text = text
        self.cmd_args = cmd_args
        self.from_user = from_user


def cmd_help(message):
    print("Доступные команды:")
    for command_name in COMMANDS:
        print(f"* {command_name}")


def cmd_weather(message):
    print(f"{message.from_user.username}, у нас хорошая погода!")


def cmd_whatisyourname(message):
    print("My name is simple bot")


def cmd_add(message):
    numbers = [int(x) for x in message.cmd_args.split()]
    print(f"Сумма чисел = {numbers[0] + numbers[1]}")


COMMANDS = {
    "/help": cmd_help,
    "/weather": cmd_weather,
    "/whatisyourname": cmd_whatisyourname,
    "/add": cmd_add,
}


def main():
    print("Hello, I'm a bot.")
    print("What is your name?")
    name = input()
    print(f"Hello, {name}")

    while True:
        text = input()
        cmd_parsed = text.split(" ", 1)
        if len(cmd_parsed) == 2:
            cmd_name, cmd_args = cmd_parsed
        else:
            cmd_name = text
            cmd_args = ""
        if cmd_name not in COMMANDS:
            print(f"Неизвестная команда: {cmd_name}")
            continue
        cmd_func = COMMANDS[cmd_name]
        # message = {"cmd_args": cmd_args, "text": text, "from_user": {"username": name}}
        message = Message(text, cmd_args, User(name))
        cmd_func(message)


main()
