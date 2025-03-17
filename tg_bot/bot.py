import time
import telebot
import config
import help
import shop
import info

bot = telebot.TeleBot(config.TOKEN)

# Словарь команд
COMMANDS = {
    "add": lambda msg: shop.message_add(msg.text, msg.chat.id) or f"Мне не понятен запрос, {msg.text},\nиспользуй help add",
    "shop": lambda msg: shop.message_shop(msg.text, msg.chat.id),
    "auto": lambda _: "Данный модуль еще в разработке",
    "help": lambda msg: help.help_message(msg.text),
    "poket": lambda _: "Данный модуль еще в разработке",
    "info": lambda msg: info.info_manager(msg.text),
}

@bot.message_handler(func=lambda message: message.text and message.chat.id in config.ACCESS_LIST)
def handle_messages(message):
    text = message.text.lower()
    try:
        for command, func in COMMANDS.items():
            if text.startswith(command):
                bot.send_message(message.chat.id, func(message))
                return
    except Exception as e:
        bot.send_message(message.chat.id, f"Что то пошло не так, ошибка:\n{e}")

    bot.send_message(message.chat.id, f"Я не знаю этой команды:\n{message.text}\nдля помощи напиши help")

def start_bot():
    print("Started TG bot")
    while True:
        try:
            bot.polling(none_stop=True, timeout=60)  # Увеличиваем таймаут
        except Exception as e:
            print(f"Ошибка: {e}")
            time.sleep(5)  # Ждем 5 секунд перед повторным запуском
            continue
        finally:
            print("TG bot stopped")

def start_bot_for_coding():
    print("Started TG bot")
    bot.polling(none_stop=True, timeout=60)  # Увеличиваем таймаут
    print("TG bot stopped")

if __name__ == '__main__':
    start_bot()
