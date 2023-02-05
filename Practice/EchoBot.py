# For import, install telebot library - pip3 install --user pytelegrambotapi
import telebot

token = "<TOKEN_HERE>"

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def echo(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)