import tkinter as tk
from tkinter import messagebox
import csv
import os

# File to store expenses
EXPENSE_FILE = "expenses.csv"

# Function to load expenses from the file
def load_expenses():
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, mode="r") as file:
            reader = csv.reader(file)
            expenses = list(reader)
        return expenses
    else:
        return []

# Function to save expenses to the file
def save_expenses(expenses):
    with open(EXPENSE_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(expenses)

# Function to add an expense
def add_expense():
    date = entry_date.get()
    category = entry_category.get()
    amount = entry_amount.get()

    if not date or not category or not amount:
        messagebox.showwarning("Input Error", "Please fill all fields!")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showwarning("Input Error", "Amount must be a number!")
        return

    expenses.append([date, category, amount])
    save_expenses(expenses)
    messagebox.showinfo("Success", "Expense added successfully!")
    entry_date.delete(0, tk.END)
    entry_category.delete(0, tk.END)
    entry_amount.delete(0, tk.END)

# Function to view all expenses
def view_expenses():
    if not expenses:
        messagebox.showinfo("Expenses", "No expenses found.")
    else:
        expense_list = "\n".join([f"Date: {e[0]}, Category: {e[1]}, Amount: ${e[2]}" for e in expenses])
        messagebox.showinfo("All Expenses", expense_list)

# Function to calculate total expenses
def calculate_total():
    total = sum(float(e[2]) for e in expenses)
    messagebox.showinfo("Total Expenses", f"Total Expenses: ${total:.2f}")

# Initialize Tkinter
root = tk.Tk()
root.title("Expense Tracker")

# Load existing expenses
expenses = load_expenses()

# Create GUI elements
label_date = tk.Label(root, text="Date (YYYY-MM-DD):")
label_date.grid(row=0, column=0, padx=10, pady=10)

entry_date = tk.Entry(root)
entry_date.grid(row=0, column=1, padx=10, pady=10)

label_category = tk.Label(root, text="Category:")
label_category.grid(row=1, column=0, padx=10, pady=10)

entry_category = tk.Entry(root)
entry_category.grid(row=1, column=1, padx=10, pady=10)

label_amount = tk.Label(root, text="Amount:")
label_amount.grid(row=2, column=0, padx=10, pady=10)

entry_amount = tk.Entry(root)
entry_amount.grid(row=2, column=1, padx=10, pady=10)

button_add = tk.Button(root, text="Add Expense", command=add_expense)
button_add.grid(row=3, column=0, columnspan=2, pady=10)

button_view = tk.Button(root, text="View Expenses", command=view_expenses)
button_view.grid(row=4, column=0, columnspan=2, pady=10)

button_total = tk.Button(root, text="Calculate Total", command=calculate_total)
button_total.grid(row=5, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()