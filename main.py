# main.py
from tg_bot.bot import start_bot

if __name__ == '__main__':
    start_bot()



# # Работа с оборотом денег в магазине add shop_name amount.
# def function_add(message: str, user_id: int, name: str) -> None:
#     message_ = message.split()
#     if message_[1].lower() == "help":
#         bot.send_message(user_id, f"Эта команда добавяет расходы в таблицу."
#                                   f" Команда должна выглядеть: 'add shop_name amount'")
#     elif message_[1].lower() == "auto":
#         work_with_auto(message, user_id, name)
#     elif len(message_) == 3 or len(message_) == 4 and is_num(message_[2]):
#         if len(message_) == 3:
#             add_money_to_shop(user_id, message_[1], float(replace_punkt(message_[2])), name)
#         else:
#             add_money_to_shop(user_id, message_[1], float(replace_punkt(message_[2])), name, message_[3])
#     else:
#         bot.send_message(user_id, f"Уточните ваш запрос: {' '.join(message_)}")
#
#
# def add_money_to_shop(user_id, shop_name: str, amount: float, name: str, note: str = None) -> None:
#     bot.send_message(user_id, f"Func add_money_to_shop started shop_name: {shop_name},"
#                               f" amount: {amount}. Username: {name}. User_id: {user_id} note:{note}")
#
# # Работа с оборотм денег авто add auto amount km what_is_done
# def work_with_auto(mesage: str, user_id: int, name: str) -> None:
#     mesage = mesage.split()
#     if mesage[1] == "auto" and len(mesage) > 2:
#         amount = float(replace_punkt(mesage[2]))
#         km = int(mesage[3])
#         start = 11 + len(mesage[2]) + len(mesage[3])
#         text = " ".join(mesage)[start::]
#         bot.send_message(user_id, f"add: amount:{amount}, km:{km}, text:{text}")
#     else:
#         bot.send_message(user_id, "add auto help - use for help")
# # Работа с оборотм денег в кошельке
# # poket info
# def work_with_wallet(message: str, user_id: int, name: str) -> None:
#     if message[0:11].lower() == "wallet help":
#         bot.send_message(user_id, "wallet add amount message - add money to poket"
#                                   "\nwallet info - show how much money have you in poket"
#                                   "\nwallet cash - take money from card")
#     else:
#         bot.send_message(user_id, "wallet help - use for help.")
# # Работа с базами данных магазинов
# def work_with_shop(message: str, user_id: int, name: str) -> None:
#     pass


# @bot.message_handler(func=lambda message: message.chat.id in ACCESS_LIST)
# def handle_messages(message):
#     if message.text[0:3].lower() == "add":
#         function_add(message.text, message.chat.id, load_names(message.chat.id))
#     elif message.text[0:4].lower() == "help":
#         bot.send_message(message.chat.id, f"add - внесение расходов.\nwallet - менеджер кошелька.\ncar - менеджер авто."
#                                           f"\nping - проверка работы робота."
#                                           f"\nК каждой комманде дописать help получишь инфо о этой команде.")
#     elif message.text[0:4].lower() == "shop":
#         work_with_shop(message.text, message.chat.id, load_names(message.chat.id))
#     elif message.text[0:6].lower() == "wallet":
#         work_with_wallet(message.text, message.chat.id, load_names(message.chat.id))
#     elif message.text[0:4].lower() == "ping":
#         bot.send_message(message.chat.id, f"{load_names(message.chat.id)}, я работаю.")
#     else:
#         bot.send_message(message.chat.id, f"{load_names(message.chat.id)}, команда: '{message.text}' не понятна")
