import sqlite3
from functools import wraps


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


# def qwert(text):
#     match = re.match(r"(\w+) (\d+,\d+) (\w+) id:(\d+)", text)
#     print(match.group(0))
#     print(match.group(1))
#     print(match.group(2))
#     print(match.group(3))
#     print(match.group(4))
#     return (match)
#
#
# print(qwert("lidl 12,32 ca id:123456"))