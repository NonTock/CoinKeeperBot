import sqlite3

def create_db():
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
    connection.commit()
    connection.close()

def add_expense(user_id, amount, category):
    connection = sqlite3.connect("coinkeeper.db")
    cursor = connection.cursor()
    cursor.execute('INSERT INTO expenses (user_id, amount, category) VALUES (?, ?, ?)', (user_id, amount, category))
    connection.commit()
    connection.close()
def get_amount(user_id):
    connection = sqlite3.connect("coinkeeper.db")
    cursor = connection.cursor()
    cursor.execute('''
    SELECT SUM(amount) FROM expenses WHERE user_id = ?
    ''', (user_id,)
    )
    result = cursor.fetchone()
    connection.close()
    return result[0]
def get_resent(user_id):
    connection = sqlite3.connect("coinkeeper.db")
    cursor = connection.cursor()
    cursor.execute('''
    SELECT amount, category FROM expenses WHERE user_id = ? ORDER BY id DESC''',
                                            (user_id,)
    )
    result = cursor.fetchmany(5)
    connection.close()
    return result