import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
    )
''')

# Удалял ранее внесенные записи, чтобы не загромождать БД при экспериментах
# cursor.execute("DELETE FROM Users")

for count in range(1, 11):
    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f'User{count}', f'example{count}@gmail.com', f'{10 * count}', 1000))
for count in range(1, 11, 2):
    cursor.execute('UPDATE Users SET balance = ? WHERE username = ?', (500, f'User{count}'))

for count in range(1, 11, 3):
    cursor.execute('DELETE FROM Users WHERE Username = ?', (f'User{count}',))

cursor.execute('SELECT Username, email, age, balance FROM Users WHERE age != ?', (60,))

cursor.execute('DELETE FROM Users WHERE id = ?', (6,))

cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]
cursor.execute('SELECT SUM(balance) FROM Users')
all_balance = cursor.fetchone()[0]
cursor.execute('SELECT AVG(balance) FROM Users')

avg_balance = cursor.fetchone()[0]
# print(avg_balance)
print(all_balance / total_users)

connection.commit()
connection.close()
