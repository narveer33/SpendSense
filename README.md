#  Personal Expense Tracker (Python + SQLite)

A simple command-line application built using **Python** and **SQLite** to help users manage and monitor their daily expenses. This lightweight tool allows users to add, view, filter, update, and delete expenses through an intuitive menu-driven interface. All data is stored locally using an SQLite database, making it fast and completely offline.

---

## 📌 Key Features

*  Add new expenses with amount, category, description, and date
*  View all expenses in a list
*  Filter expenses by **category** or **date**
*   Update existing expense entries
*  Delete expenses by ID
*  All data saved in a local **SQLite database**
*  Built entirely with **built-in Python libraries** — no extra installation required

---

## 🛠️ Technologies Used

| Technology     | Purpose                            |
| -------------- | ---------------------------------- |
| Python         | Core programming language          |
| SQLite3        | Lightweight local database         |
| CLI (Terminal) | User interaction (text-based menu) |

---

## 🧱 Project Structure

```
 expense-tracker/
├── db.py           # Creates the SQLite database and table
├── functions.py    # Contains all the database operations (add, view, update, delete)
├── main.py         # Main CLI program with menu loop
└── README.md       # Project documentation
```

---

## 🚀 How to Run

### Step 1: Clone or Download

```bash
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker
```

### Step 2: Create the Database

Run the following once to set up the database:

```bash
python db.py
```

### Step 3: Start the Expense Tracker

```bash
python main.py
```

---

## 🧪 Sample Data Entry

When adding a new expense:

```
Amount: 150
Category: Food
Description: Lunch with friends
Date (YYYY-MM-DD): 2025-06-30
```

When viewing expenses:

```
(1, 150.0, 'Food', 'Lunch with friends', '2025-06-30')
```

---

## 📊 Example Menu Interface

```text
Personal Expense Tracker
1. Add Expense
2. View All Expenses
3. Filter by Category
4. Filter by Date
5. Update an Expense
6. Delete an Expense
7. Exit
```

---

## 🎯 Learning Outcomes

* Working with **SQLite** databases using Python
* Implementing **CRUD operations**
* Structuring a Python project with modular code
* Building a **menu-driven CLI app**
* Understanding how to persist user data

---

## 🌟 Future Improvements (optional)

* Export to CSV or Excel
* Monthly/Yearly expense summaries
* Graphs (Pie chart or bar chart by category)
* GUI interface using Tkinter or PyQt

---

## 🙋‍♂️ Author

**Narveer Singh**
*M.Sc. Economics | Python Developer*

