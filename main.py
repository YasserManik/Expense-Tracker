class ExpenseTracker:
    """
    A simple expense tracker that allows users to add and track their expenses.
    Uses a list to store each expense, where each expense is a dictionary.
    """

    def __init__(self):
        """Initialises the expense tracker with an empty list of expenses."""

        self.expenses = []

    def add_expense(self):
        """Prompts user input for expense and its description, adding them to the list."""


        description = input("Enter the description of the expense: ")

        # Handling invalid input for amount
        while True:
            try:
                amount = float(input("Enter expense amount: £"))
                # Handing negative input
                if amount < 0:
                    print("Amount cannot be negative, please try again.")
                else:
                    break
            # Handling non-numerical input
            except ValueError:
                print("Invalid input, please enter a numerical amount.")

        # Add the expense to the list as a dictionary
        self.expenses.append({"description": description, "amount": amount})
        print("\nExpense added!\n")

    def show_expenses(self):
        """Outputs all expenses stored in tracker."""

        # Check if there are any expenses stored
        if not self.expenses:
            print("No expenses added\n")
            return

        # Display all expenses with their index, description and amount
        print("----ALL EXPENSES----\n")
        for index, expense in enumerate(self.expenses, start=1):
            print(f"{index}. {expense['description']}: £{expense['amount']:.2f}")

    def calculate_total(self):
        """Calculate and display total amount spent on expenses."""

        # Sum the amount of all expenses stored
        total = sum(expense["amount"] for expense in self.expenses)

        # Display the total amount spent
        print(f"\nTotal amount spent: £{total:.2f}\n")

    def run(self):
        """Runs the main loop of the expense tracker, showing the main menu and handling user input."""

        while True:
            print("Welcome to the expense tracker!")
            print("1. Add expense")
            print("2. Show expenses")
            print("3. Show total expense")
            print("4. Exit expense tracker")

            # Takes user input of their menu choice
            choice = input("choose an option 1-4: ")

            # Handing of user's choice
            if choice == "1":
                self.add_expense()
            elif choice == "2":
                self.show_expenses()
            elif choice == "3":
                self.calculate_total()
            elif choice == "4":
                print("Exiting the expense tracker.")
                break # Exit the loop and terminate the program
            else:
                # Handling invalid input
                print("Invalid input, please try again\n")

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()