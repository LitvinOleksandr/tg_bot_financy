import telebot
import config
import help
import shop
import info

bot = telebot.TeleBot(config.TOKEN)

# Словарь команд
COMMANDS = {
    "add": lambda msg: shop.message_add(msg.text, msg.chat.id) or f"i don't understand {msg.text},\nuse help",
    "shop": lambda msg: shop.message_shop(msg.text, msg.chat.id),
    "auto": lambda _: "Данный модуль еще в разработке",
    "help": lambda msg: help.help_message(msg.text),
    "poket": lambda _: "Данный модуль еще в разработке",
    "info": lambda msg: info.info_computer(msg.text),
}

@bot.message_handler(func=lambda message: message.text and message.chat.id in config.ACCESS_LIST)
def handle_messages(message):
    text = message.text.lower()

    for command, func in COMMANDS.items():
        if text.startswith(command):
            bot.send_message(message.chat.id, func(message))
            return

    bot.send_message(message.chat.id, f"Я не знаю этой команды:\n{message.text}\nдля помощи напиши help")

def start_bot() -> None:
    print("Started TG bot")
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        print("TG bot stopped")

if __name__ == '__main__':
    start_bot()