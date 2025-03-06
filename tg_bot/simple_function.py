import sqlite3
from functools import wraps
from shop import add_shop


#decorator
def with_db_connection(db_path='../db.sqlite3'):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
                result = func(cursor, *args, **kwargs)
                return result
        return wrapper
    return decorator


def replace_punkt_to_comma(stroka: str) -> str:
    return stroka.replace(",", ".")

def is_num(numer) -> bool:
    numer = replace_punkt_to_comma(numer)
    try:
        float(numer)
        return True
    except ValueError:
        print("not num")
        return False

def auto_makes_request(message: str) -> list:
    #out [str, float, int]
    message = message[5::]
    i = 0
    while i < len(message):
        if not message[i].isdigit():
            i += 1
            continue
        break
    mes = message[0:i - 1]
    message = message[i::].split()
    return [mes, float(replace_punkt_to_comma(message[0])), int(message[1])]

def from_list_to_str(data_input) -> str:
    text_spending_by_shop = ""
    for shop, total in data_input:
        text_spending_by_shop += f"{shop} - {total}\n"
    return text_spending_by_shop

def make_date_to_db(month: str, year: str) -> list[str]:
    if len(month) == 1:
        month = f"0{month}"
    start_date = f"{year}-{month}-01 00:00:00"
    end_date = f"{year}-{month}-31 23:59:59"
    return [start_date, end_date]

def create_day_to_db(month: int, day: int) -> str:
    if day < 10:
        day = f"0{day}"
    else:
        day = f"{day}"
    return f"2025-0{month}-{day} 12:00:00"

def manualy_add_to_db(array:list, month: int):
    for cell in array:
        add_shop(
            shop_name=cell[0],
            amount=cell[1],
            money_from=cell[2],
            customer_id=cell[3],
            created_at=create_day_to_db(month=month, day=cell[4])
        )