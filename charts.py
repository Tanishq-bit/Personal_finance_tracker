import sqlite3
import matplotlib.pyplot as plt

def show_expense_chart():
    conn = sqlite3.connect("expenses.db")
    c = conn.cursor()
    c.execute("SELECT category, SUM(amount) FROM transactions WHERE type='Expense' GROUP BY category")
    data = c.fetchall()
    conn.close()

    if data:
        categories, amounts = zip(*data)
        plt.figure(figsize=(6,6))
        plt.pie(amounts, labels=categories, autopct="%1.1f%%")
        plt.title("Expenses by Category")
        plt.show()
    else:
        print("No expense data to display.")
