import sqlite3


def initiate_db():
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
    # Заполнение базы данных
    for i in range(1, 5):
        cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                       (f"Продукт {i}", f"Описание {i}", f"{100 * i}"))
    #     # Удаление из БД products.db записи id более 4 (что бы избежать множественных записей при повторном вызове):
        cursor.execute("DELETE FROM products WHERE id > 4")

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')
    # Автоматическое добавление пользователей
    # for i in range(7):
    #    cursor.execute("INSERT INTO Users (username, email, age) VALUES (?, ?, ?)", (f"newuser{i}", f"{i}ex@gmail.com", str(random.randint(20, 60))))
    connection.commit()
    connection.close()


def add_user(username, email, age):
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO Users (username, email, age, balance) VALUES ('{username}', '{email}', '{age}', 1000)")
    connection.commit()


def is_included(username):
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()
    check_user = cursor.execute(f"SELECT * FROM Users WHERE username=?", (username,))
    if check_user.fetchone() is None:
        return False
    else:
        return True


def get_all_products():
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM Products")
    all_products = cursor.fetchall()
    return all_products

    connection.commit()
    connection.close()
