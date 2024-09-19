# **Expense Tracker**

A simple Python-based expense tracker that allows users to add, display, and calculate total expenses. The tracker stores each expense as a dictionary with a description and an amount, and provides an interactive console interface.

## Table of Contents

1. [Project Overview](/main/README.md/content/Expense-Tracker#Project-Overview)
2. [Features](/main/README.md/content/Expense-Tracker#Features)
3. [Installation](/main/README.md/content/Expense-Tracker#Features)
4. [Usage](/main/README.md/content/Expense-Tracker#Usage)
5. [Contributing](/main/README.md/content/Expense-Tracker#Contributing)

# Project Overview
This Expense Tracker is designed to help users easily manage and track their spending. It uses a simple interface for adding expenses, displaying a list of all expenses, and calculating the total amount spent.

Users can interact with the program through a menu that allows them to:

* Add new expenses.
* View all expenses.
* Calculate and view the total amount spent.
* Exit the application.

## Features
* **Add Expenses**: Add an expense by specifying a description and amount. Input is validated to prevent invalid or negative values.
* **View Expenses**: Display a list of all expenses, each with a description and amount.
* **Calculate Total**: Calculate and display the total of all expenses added.
* **Input Validation**: Ensures that entered amounts are valid numbers and not negative.

## Installation

1. Clone the repository:

        git clone https://github.com/your-username/expense-tracker.git
      
        cd expense-tracker

2. No external dependencies are required. Just ensure you have Python 3.x installed on your machine.

## Usage

To run the program, execute the following command in your terminal:

    python expense_tracker.py

## Menu Options
Upon running the program, you will see the following menu:
    
    Welcome to the expense tracker!
        
        1. Add expense
        2. Show expenses
        3. Show total expense
        4. Exit expense tracker

* **Option 1**: Add a new expense by entering a description and a valid amount.
* **Option 2**: View all previously added expenses.
* **Option 3**: Calculate and display the total of all added expenses.
* **Option 4**: Exit the program.

## Example

    Welcome to the expense tracker!
    1. Add expense
    2. Show expenses
    3. Show total expense
    4. Exit expense tracker
    choose an option 1-4: 1
    Enter the description of the expense: Lunch
    Enter expense amount: £12.50

    Expense added!
    
    Welcome to the expense tracker!
    1. Add expense
    2. Show expenses
    3. Show total expense
    4. Exit expense tracker
    choose an option 1-4: 2
    ----ALL EXPENSES----
    1. Lunch: £12.50

## Contributing
Contributions are welcome! Please follow the steps below:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-name).
3. Commit your changes (git commit -m "Added new feature").
4. Push to the branch (git push origin feature-name).
5. Open a pull request.
