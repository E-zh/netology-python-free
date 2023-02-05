# For import, install telebot library - pip3 install --user pytelegrambotapi
from random import choice
import telebot


token = "<TOKEN_HERE>>"
bot = telebot.TeleBot(token)
HELP = """
/help - вывести список доступных команд.
/add - добавить задачу в список (формат: /add дата задача Категория).
/show - показать все добавленные задачи.
/random - добавить случайную задачу на дату Сегодня."""
RANDOM_TASKS = ["Записаться на курс в Нетологию", "Написать Гвидо письмо", "Покормить кошку", "Помыть машину"]
RANDON_CATEGORY = ["Домашнее", "Работа", "Учеба"]
tasks = {}


def add_todo(date, task, category):
    if date in tasks:
        tasks[date].append(task + " " + "@" + category)
    else:
        tasks[date] = []
        tasks[date].append(task + " " + "@" + category)


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=["add"])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    mess = command[2].split()
    category = mess[-1]
    mess.pop(-1)
    task = " ".join(mess)
    if len(task) >= 3:
        add_todo(date, task, category)
        text = "Задача " + task + " добавлена на дату " + date
    else:
        text = "Ошибка! Задача должна содержать не менее 3-х символов!"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["random"])
def random_add(message):
    date = "сегодня"
    task = choice(RANDOM_TASKS)
    category = choice(RANDON_CATEGORY)
    add_todo(date, task, category)
    text = "Задача " + task + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["show", "print"])
def show(message):
    command = message.text.split()
    command.pop(0)
    for date in command:
        if date in tasks:
            text = date.upper()+":\n"
            for task in tasks[date]:
                text = text + "[] " + task + "\n"
        else:
            text = "Задач на " + date.upper() + " нет"
        bot.send_message(message.chat.id, text)


# Постоянное обращение к серверам Telegram
bot.polling(none_stop=True)
