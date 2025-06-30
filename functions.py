import sqlite3

# Add expense
def add_expense(amount, category, description, date):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?, ?)",
                   (amount, category, description, date))
    conn.commit()
    conn.close()
   

# View all
def view_expenses():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    data = cursor.fetchall()
    conn.close()
    return data

# Filter by category
def filter_by_category(category):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses WHERE category = ?", (category,))
    data = cursor.fetchall()
    conn.close()
    return data

# Filter by date
def filter_by_date(date):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses WHERE date = ?", (date,))
    data = cursor.fetchall()
    conn.close()
    return data

# Update an expense
def update_expense(expense_id, amount, category, description, date):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE expenses SET amount=?, category=?, description=?, date=? WHERE id=?
    """, (amount, category, description, date, expense_id))
    conn.commit()
    conn.close()

# Delete an expense
def delete_expense(expense_id):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id=?", (expense_id,))
    conn.commit()
    conn.close()
