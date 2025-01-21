# module_14_2.py
# 21.01.2025 Задача "Средний баланс пользователя":

import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# Заполнение базы данных
# for i in range(1, 11):
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{i}",
#                                                                                              f"example{i}@gmail.com",
#                                                                                              f"{i}0", 1000))

# Обновите balance у каждой 2ой записи начиная с 1ой на 500
# for i in range(1, 11, 2):
#     cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, f"{i}"))

# Удалите каждую 3ую запись в таблице начиная с 1ой:
# for i in range(1, 11, 3):
#     cursor.execute("DELETE FROM Users WHERE id = ?", (f"{i}",))

# Сделайте выборку ви выведете в консоль
# cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))
# users = cursor.fetchall()
# for user in users:
#     print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}")

# 1. Удалите из базы данных not_telegram.db запись с id = 6.:
# cursor.execute("DELETE FROM Users WHERE id = ?", (6,))

# 2. Подсчитать общее количество записей.
# cursor.execute("SELECT COUNT(*) FROM Users")
# total_users = cursor.fetchall()[0]
# print(f"Общее количество записей: {total_users[0]}")

# 3. Посчитать сумму всех балансов.
# cursor.execute("SELECT SUM(balance) FROM Users")
# all_balance = cursor.fetchall()[0]
# print(f"Сумма всех балансов: {all_balance[0]}")

# 4. Вывести в консоль средний баланс всех пользователей.
# 4.1.
cursor.execute("SELECT AVG(balance) FROM Users")
average_balance = cursor.fetchall()[0]
print(f"Средний баланс всех пользователей: {average_balance[0]}")
# 4.2.
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchall()[0]
cursor.execute("SELECT SUM(balance) FROM Users")
all_balance = cursor.fetchall()[0]
print(f"Средний баланс всех пользователей: {all_balance[0] / total_users[0]}")

connection.commit()
connection.close()
