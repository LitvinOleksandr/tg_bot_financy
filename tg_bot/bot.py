import telebot

from config import TOKEN, ACCESS_LIST, load_names
from help import help_message
from shop import *
from auto import *
from poket import *


bot = telebot.TeleBot(TOKEN)


def auto(title: str, amount: float, km: int) -> None:
    pass

@bot.message_handler(func=lambda message: message.chat.id in ACCESS_LIST)
def handle_messages(message):
    if message.text[0:3].lower() == "add":
        if not message_add(message.text, message.chat.id):
            bot.send_message(message.chat.id, f"i don't understand {message.text},"
                                              f"\nuse help")
    elif message.text[0:4].lower() == "shop":
        bot.send_message(message.chat.id, message_shop(message.text, message.chat.id))
    elif message.text[0:4].lower() == "auto":
        bot.send_message(message.chat.id, "Данный модуль еще в разработке")
    elif message.text[0:4].lower() == "help":
        bot.send_message(message.chat.id, help_message(message.text))
    elif message.text[0:5].lower() == "poket":
        bot.send_message(message.chat.id, "Данный модуль еще в разработке")
    else:
        bot.send_message(message.chat.id, f"Я не знаю этой команды:\n{message.text}\n"
                                          f"для помощи напиши help")

def start_bot() -> None:
    print("Started tg bot")
    bot.polling(none_stop=True)
    print("Tg bot stopped")

if __name__ == '__main__':
    start_bot()
