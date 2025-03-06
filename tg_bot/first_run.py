import sqlite3
import os

TOKEN = "your-telegram-bot-token"
ACCESS_LIST = [123, 456, 789]


def create_new_db_bot_shop() -> None:
    # Подключаемся к базе данных (если файла нет, он будет создан)
    db_name = "../db.sqlite3"
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Создаем таблицу bot_shop, если она еще не существует
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS bot_shop (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        shop TEXT NOT NULL,
        amount REAL NOT NULL,
        type_payment TEXT NOT NULL,
        id_customer INTEGER NOT NULL,
        created_at TEXT NOT NULL
    )
    ''')

    # Сохраняем изменения и закрываем соединение
    conn.commit()
    conn.close()

    print(f"Database '{db_name}' and table 'bot_shop' have been created successfully.")

def create_token_file(token):
    """Создает файл token.txt и записывает в него токен."""
    with open("token2.txt", "w") as file:
        file.write(token)
    print("File 'token.txt' has been created successfully.")

def create_access_list_file(access_list):
    """Создает файл access_list.txt и записывает в него список ID построчно."""
    with open("access_list.txt", "w") as file:
        for user_id in access_list:
            file.write(str(user_id) + "\n")
    print("File 'access_list.txt' has been created successfully.")

if __name__ == "__main__":
    create_new_db_bot_shop()
    create_token_file(token=TOKEN)
    create_access_list_file(access_list=ACCESS_LIST)
    # Удаление самого себя
    script_path = os.path.abspath(__file__)  # Получаем путь к текущему файлу
    os.remove(script_path)  # Удаляем файл

    print("Setup completed! 'first_run.py' has been deleted.")