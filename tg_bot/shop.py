import datetime
from datetime import datetime, timedelta, timezone
import simple_function

def message_add(mes_text: str, user_id: int):
    if (mes_text[0:3].lower() == "add" and len(mes_text.split()) == 4
            or mes_text[0:3].lower() == "add" and len(mes_text.split()) == 3):
        mess = mes_text.split()
        if len(mess) == 3 and simple_function.is_num(mess[2]) or len(mess) == 4 and simple_function.is_num(mess[2]):
            add_shop(
                shop_name=mess[1],
                amount=float(simple_function.replace_punkt_to_comma(mess[2])),
                money_from="cash" if len(mess) == 4 else "card",
                customer_id=user_id,
                created_at=None
            )
            return f"{simple_function.replace_punkt_to_comma(mess[2])} € успешно добавлены в {mess[1]}"
    return False

def message_shop(mes_text: str, user_id: int) -> str:
    message = mes_text.lower().split()
    text_message = "use: help shop"
    if len(message) == 3 and message[1] == "info":
        text_message = (f"{simple_function.from_list_to_str(get_spending_by_shop(month=message[2]))}"
                        f"\ntotal = {get_total_spent_in_shop(month=message[2])}")
    return text_message


####################################################################################
#           Use database injection                                                 #
####################################################################################
#
# Добавляем данные в таблицу
# add_shop(
#     shop_name="Name", Пишем имя магазина. удобней мелкими буквами.
#     amount=12.34, используем float тип данных
#     money_from="cash", на выбор "cash" or "card". Автоматически пищет карта
#     customer_id=123456, Берется id того кто пишет смс боту
#     created_at="2025-01-01 00:00:00" Если не указано дата, она ставится автоматически в данный момент
# )
####################################################################################
@simple_function.with_db_connection()
def add_shop(cursor, shop_name, amount, money_from, customer_id, created_at = None):
    # Получаем текущее время с учетом часового пояса
    if not created_at:
        created_at = datetime.now(timezone(timedelta(hours=1))).strftime('%Y-%m-%d %H:%M:%S')
    # Выполняем запрос
    cursor.execute('''
    INSERT INTO bot_shop (shop, amount, type_payment, id_customer, created_at)
    VALUES (?, ?, ?, ?, ?)
    ''', (shop_name, amount, money_from, customer_id, created_at))


# Чтение данных из таблицы
@simple_function.with_db_connection()
def get_shops(cursor):
    cursor.execute("SELECT * FROM bot_shop")  # Заменить bot_shop на имя своей таблицы
    return cursor.fetchall()

####################################################################################
#Вывод всех магазинов и сумма денег потраченых в них.
#spending = get_spending_by_shop(month="02")
#year автоматом стоит 2025, при необходимости можно изменить.
####################################################################################
@simple_function.with_db_connection()
def get_spending_by_shop(cursor, month: str, year: str="2025"):
    start_date, end_date = simple_function.make_date_to_db(month=month, year=year)

    cursor.execute('''
        SELECT shop, SUM(amount) AS total_spent
        FROM bot_shop
        WHERE created_at BETWEEN ? AND ?
        GROUP BY shop
        ORDER BY total_spent DESC;
    ''', (start_date, end_date))
    return cursor.fetchall()  # Вернем список кортежей (shop, total_spent)

####################################################################################
# get_total_spent_in_shop(month="03", year="2025")
# выводит сумму за весь месяц всех магазинов. Если нет никаких данных выводит 0
####################################################################################
@simple_function.with_db_connection()
def get_total_spent_in_shop(cursor, month: str, year = "2025"):
    start_date, end_date = simple_function.make_date_to_db(month=month, year=year)

    cursor.execute('''
        SELECT SUM(amount) AS total_spent
        FROM bot_shop
        WHERE created_at BETWEEN ? AND ?;
    ''', (start_date, end_date))

    result = cursor.fetchone()  # Получаем одну строку
    return round(result[0], 2) if result[0] is not None else 0  # Если нет данных, вернуть 0
