import sqlite3

connection = sqlite3.connect("coinkeeper.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS expenses (
id INTEGER PRIMARY KEY,
user_id INTEGER,
amount REAL,
category TEXT
)
''')
def add_expense(user_id, amount, category):
    connection = sqlite3.connect("coinkeeper.db")
    cursor = connection.cursor()
    cursor.execute('INSERT INTO expenses (user_id, amount, category) VALUES (?, ?, ?)', (user_id, amount, category))
    connection.commit()
    connection.close()

connection.commit()
connection.close()