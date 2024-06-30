from abc import ABC, abstractmethod
from decorators import log_operation
import sqlite3

# Abstract base class representing a bank account
class BankAccount(ABC):
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number  # Unique identifier for the account
        self.account_holder = account_holder  # Name of the account holder
        self.balance = balance  # Initial balance
        self.branch = None  # Branch information, initially set to None

    @abstractmethod
    def account_type(self):
        # Abstract method to be implemented by subclasses to specify account type
        pass

    @log_operation
    def deposit(self, amount):
        # Method to deposit an amount into the account
        self.balance += amount
        self.save()  # Save account details to the database
        if self.branch:
            self.branch.deposit_to_investment(amount)  # Update branch investment
        print(f"Deposited {amount}. New balance is {self.balance}.")

    @log_operation
    def withdraw(self, amount):
        # Method to withdraw an amount from the account
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            self.save()  # Save account details to the database
            if self.branch:
                self.branch.withdraw_from_investment(amount)  # Update branch investment
            print(f"Withdrew {amount}. New balance is {self.balance}.")

    def save(self):
        # Save account details to the database
        with sqlite3.connect('bank.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS accounts
                              (account_number TEXT, account_holder TEXT, balance REAL, account_type TEXT, branch TEXT)''')
            cursor.execute('''INSERT OR REPLACE INTO accounts VALUES (?, ?, ?, ?, ?)''',
                           (self.account_number, self.account_holder, self.balance, self.account_type(), self.branch.name if self.branch else None))
            conn.commit()

# Savings account class inheriting from BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate  # Interest rate for the savings account

    def account_type(self):
        return "Savings"

    def add_interest(self):
        # Method to add interest to the balance
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.save()  # Save account details to the database
        print(f"Interest added {interest}. New balance is {self.balance}.")

# Checking account class inheriting from BankAccount
class CheckingAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0):
        super().__init__(account_number, account_holder, balance)

    def account_type(self):
        return "Checking"
