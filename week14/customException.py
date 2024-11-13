# Step 1: Define a custom exception class
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"Attempted to withdraw {amount}, but only {balance} is available.")
        self.balance = balance
        self.amount = amount

# A simple bank account class
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Current balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            # Step 2: Raise the custom exception if withdrawal amount exceeds balance
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        print(f"Withdrew {amount}. Current balance: {self.balance}")

# Step 3: Handling the custom exception
try:
    account = BankAccount(100)  # Account starts with $100
    account.deposit(50)         # Deposit $50, balance becomes $150
    account.withdraw(200)       # Attempt to withdraw $200 (which is more than the available balance)
except InsufficientFundsError as e:
    print(f"Error: {e}")        # Custom error message will be printed