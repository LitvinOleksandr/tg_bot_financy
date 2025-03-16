import telebot
import config
import help
import shop

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(func=lambda message: message.chat.id in config.ACCESS_LIST)
def handle_messages(message):
    if message.text[0:3].lower() == "add":
        if not shop.message_add(message.text, message.chat.id):
            bot.send_message(message.chat.id, f"i don't understand {message.text},"
                                              f"\nuse help")
    elif message.text[0:4].lower() == "shop":
        bot.send_message(message.chat.id, shop.message_shop(message.text, message.chat.id))
    elif message.text[0:4].lower() == "auto":
        bot.send_message(message.chat.id, "Данный модуль еще в разработке")
    elif message.text[0:4].lower() == "help":
        bot.send_message(message.chat.id, help.help_message(message.text))
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
