import sqlite3

def init_db():
    conn = sqlite3.connect("expenses.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT NOT NULL,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        date TEXT NOT NULL,
        note TEXT
    )''')
    conn.commit()
    conn.close()

def insert_transaction(tx_type, amount, category, date, note):
    conn = sqlite3.connect("expenses.db")
    c = conn.cursor()
    c.execute("INSERT INTO transactions (type, amount, category, date, note) VALUES (?, ?, ?, ?, ?)",
              (tx_type, amount, category, date, note))
    conn.commit()
    conn.close()

def fetch_transactions():
    conn = sqlite3.connect("expenses.db")
    c = conn.cursor()
    c.execute("SELECT * FROM transactions ORDER BY date DESC")
    rows = c.fetchall()
    conn.close()
    return rows
