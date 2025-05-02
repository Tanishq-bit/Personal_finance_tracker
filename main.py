import tkinter as tk
from tkinter import ttk, messagebox
from database import init_db, insert_transaction, fetch_transactions
from charts import show_expense_chart
import datetime

init_db()

def add_transaction():
    try:
        amount = float(amount_entry.get())
        category = category_var.get()
        tx_type = type_var.get()
        date = date_entry.get()
        note = note_entry.get()

        if not date:
            date = datetime.date.today().isoformat()

        insert_transaction(tx_type, amount, category, date, note)
        messagebox.showinfo("Success", "Transaction added successfully!")
        clear_fields()
        load_transactions()
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount.")

def clear_fields():
    amount_entry.delete(0, tk.END)
    category_var.set("Food")
    type_var.set("Expense")
    note_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)

def load_transactions():
    for i in tree.get_children():
        tree.delete(i)
    for row in fetch_transactions():
        tree.insert("", tk.END, values=row)

app = tk.Tk()
app.title("Personal Finance Tracker")

# Input Fields
tk.Label(app, text="Amount").grid(row=0, column=0)
amount_entry = tk.Entry(app)
amount_entry.grid(row=0, column=1)

tk.Label(app, text="Type").grid(row=1, column=0)
type_var = tk.StringVar(value="Expense")
type_menu = ttk.Combobox(app, textvariable=type_var, values=["Income", "Expense"])
type_menu.grid(row=1, column=1)

tk.Label(app, text="Category").grid(row=2, column=0)
category_var = tk.StringVar(value="Food")
category_menu = ttk.Combobox(app, textvariable=category_var, values=["Food", "Transport", "Rent", "Shopping", "Salary", "Others"])
category_menu.grid(row=2, column=1)

tk.Label(app, text="Date (YYYY-MM-DD)").grid(row=3, column=0)
date_entry = tk.Entry(app)
date_entry.grid(row=3, column=1)

tk.Label(app, text="Note").grid(row=4, column=0)
note_entry = tk.Entry(app)
note_entry.grid(row=4, column=1)

tk.Button(app, text="Add Transaction", command=add_transaction).grid(row=5, column=0, columnspan=2, pady=5)
tk.Button(app, text="Show Expense Chart", command=show_expense_chart).grid(row=6, column=0, columnspan=2, pady=5)

# Transaction History
cols = ("ID", "Type", "Amount", "Category", "Date", "Note")
tree = ttk.Treeview(app, columns=cols, show="headings")
for col in cols:
    tree.heading(col, text=col)
tree.grid(row=7, column=0, columnspan=2)

load_transactions()
app.mainloop()
