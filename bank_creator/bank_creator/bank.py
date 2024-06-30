import sqlite3

# Class representing a bank
class Bank:
    def __init__(self, name, initial_investment=0):
        self.name = name  # Name of the bank
        self.initial_investment = initial_investment  # Initial investment amount
        self.branches = []  # List of bank branches
        self.total_investment = initial_investment  # Total investment amount
        self.setup_database()  # Setup the database for the bank

    def setup_database(self):
        # Method to setup the database for the bank
        with sqlite3.connect('bank.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS banks
                              (name TEXT, total_investment REAL)''')
            cursor.execute('''INSERT OR REPLACE INTO banks VALUES (?, ?)''',
                           (self.name, self.total_investment))
            conn.commit()

    def add_branch(self, branch):
        # Method to add a branch to the bank
        self.branches.append(branch)
        branch.bank = self
        branch.investment = self.initial_investment / len(self.branches)
        self.save()  # Save bank details to the database

    def save(self):
        # Save bank details to the database
        with sqlite3.connect('bank.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''INSERT OR REPLACE INTO banks VALUES (?, ?)''',
                           (self.name, self.total_investment))
            conn.commit()

# Class representing a bank branch
class BankBranch:
    def __init__(self, name):
        self.name = name  # Name of the branch
        self.accounts = []  # List of accounts in the branch
        self.investment = 0  # Investment amount for the branch
        self.bank = None  # Reference to the parent bank

    def add_account(self, account):
        # Method to add an account to the branch
        self.accounts.append(account)
        account.branch = self

    def deposit_to_investment(self, amount):
        # Method to deposit an amount to the branch's investment
        if self.bank:
            self.investment += amount
            self.bank.total_investment += amount
            self.bank.save()  # Save bank details to the database

    def withdraw_from_investment(self, amount):
        # Method to withdraw an amount from the branch's investment
        if amount <= self.investment:
            self.investment -= amount
            self.bank.total_investment -= amount
            self.bank.save()  # Save bank details to the database
        else:
            print("Insufficient funds in branch investment.")
