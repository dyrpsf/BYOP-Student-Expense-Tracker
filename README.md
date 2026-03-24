# Student Expense Tracker

## Problem Statement
Many college students spend money daily on food, travel, stationery, and other needs without keeping track of their expenses. This makes budgeting difficult and often leads to overspending.

## Solution
Student Expense Tracker is a command-line Python application that helps students record, manage, and analyze their daily expenses. It stores expense data in a JSON file and allows users to view summaries directly from the terminal.

## Features
- Add a new expense
- View all expenses
- Calculate total spending
- Filter expenses by category
- View monthly expense summary
- Delete an expense
- Automatic data storage using JSON

## Technologies Used
- Python 3
- JSON for local data storage
- Git and GitHub for version control

## Project Structure
```text
BYOP-Student-Expense-Tracker/
│
├── main.py
├── expense_manager.py
├── data.json
├── README.md
├── requirements.txt
└── .gitignore
```
## Setup Instructions
1. Clone the repository
```bash
git clone https://github.com/dyrpsf/BYOP-Student-Expense-Tracker.git
```

2. Navigate into the project folder
```bash
cd BYOP-Student-Expense-Tracker
```

3. Make sure Python is installed
Check Python version:
```Bash
python --version
```
4. Run the project
```Bash
python main.py
```
## How to Use
After running the program, a menu will appear:

1. Add Expense
2. View All Expenses
3. View Total Expense
4. Filter by Category
5. Monthly Summary
6. Delete Expense
7. Exit
Enter the number corresponding to the action you want to perform.

## Example Use Cases
    Track daily food and travel expenses
    Check total spending in a month
    Filter spending by category like Food, Travel, Study
    Remove incorrect entries

## Future Improvements
    Add budget alerts
    Export data to CSV
    Add graphical charts
    Build a web interface

## Author
Deepak Yadav <br>
B.Tech CSE Student <br>
VIT Bhopal University