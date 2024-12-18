# Expenses Tracker (Money Manager)

A simple Python-based expense tracking application that allows users to log their daily expenses, view all entries, search for specific entries, view summary reports, and delete unwanted entries. The application uses a CSV file (expenses.csv) to store all data and provides an interactive command-line interface for managing expenses.

Features

Log a new entry: Record an expense with the date, category, amount, and an optional description.
View all entries: Display all logged entries sorted by the most recent.
View summary: Get a summary of total expenses per category and the overall amount spent.
Search entries: Find entries by date, amount, or category.
Delete an entry: Remove an entry based on search criteria.
Installation

To use the Expense Logger, follow these steps:

Clone the repository:
git clone https://github.com/your-username/expense-logger.git
cd expense-logger
Install Python: Ensure you have Python 3.x installed on your system. You can download Python from here.
Run the application: To run the application, simply execute the following command:
python expense_logger.py
Dependencies: This project requires no external dependencies apart from Python's built-in libraries (csv, datetime, sys).
Usage

Once the application is running, you'll be presented with a menu with the following options:

Log a new entry: You will be prompted to input the date, category, amount, and description of the expense.
View all entries: Displays a list of all logged entries, sorted by date.
View summary: Displays the total expenses per category and the overall total.
Delete entry: Search for an entry by date, amount, or category, and delete it if needed.
Quit: Exit the application.
Example Output
When viewing all entries:

Saved Entries:
Date            Category        Amount    Description
18/12/24        Food            12.50     Lunch at cafe
17/12/24        Transport       5.75      Bus ticket
When viewing the summary:

Summary:
Food: $12.50
Transport: $5.75
Total spent: $18.25
File Structure

expense_logger.py: The main Python script that runs the expense logging application.
expenses.csv: A CSV file that stores all logged expense entries.
Notes

Ensure that the expenses.csv file exists before running the application. If the file is missing, the program will prompt you to create it by logging a new entry.
If you choose to delete an entry, the program will ask for confirmation before removing it permanently.
