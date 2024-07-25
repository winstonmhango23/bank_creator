 # bank_creator

The bank_creator package provides some basic set of tools for managing various types of bank accounts, including savings, checking, loan, and reward accounts. It also simulates the creation and management of banks and their branches.

## Table of Contents

- [bank\_creator](#bank_creator)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
- [Create a bank with an initial investment](#create-a-bank-with-an-initial-investment)
- [Create branches](#create-branches)
- [Add branches to the bank](#add-branches-to-the-bank)
- [Create a savings account](#create-a-savings-account)
- [Add the savings account to a branch](#add-the-savings-account-to-a-branch)
- [Create a checking account](#create-a-checking-account)
- [Add the checking account to a branch](#add-the-checking-account-to-a-branch)
- [Create a loan account](#create-a-loan-account)
- [Add the loan account to a branch](#add-the-loan-account-to-a-branch)
- [Create a reward savings account](#create-a-reward-savings-account)
- [Create a reward checking account](#create-a-reward-checking-account)
- [Add the reward accounts to branches](#add-the-reward-accounts-to-branches)
- [Deposit into savings account](#deposit-into-savings-account)
- [Withdraw from checking account](#withdraw-from-checking-account)
- [Repay loan](#repay-loan)
- [Earn rewards on reward account](#earn-rewards-on-reward-account)
- [Redeem rewards on reward account](#redeem-rewards-on-reward-account)
- [Transfer funds from one account to another](#transfer-funds-from-one-account-to-another)
- [Perform custom operation](#perform-custom-operation)

## Installation

To install the bank_creator package, use pip:

```bash
pip install bank_creator
Creating a Bank and Branches
Creating a Bank
To create a bank, instantiate the Bank class with a name and an initial investment amount:

python
Copy code
from bank import Bank

# Create a bank with an initial investment
my_bank = Bank(name="My Bank", initial_investment=100000)
Creating Branches
You can create branches for the bank using the BankBranch class and add them to the bank:

python
Copy code
from bank import BankBranch

# Create branches
branch1 = BankBranch(name="Branch 1")
branch2 = BankBranch(name="Branch 2")

# Add branches to the bank
my_bank.add_branch(branch1)
my_bank.add_branch(branch2)
Creating Accounts
Savings Account
A savings account can be created using the SavingsAccount class. It requires an account number, account holder's name, initial balance, and interest rate:

python
Copy code
from account import SavingsAccount

# Create a savings account
savings_account = SavingsAccount(account_number="123456789", account_holder="John Doe", balance=1000, interest_rate=0.03)

# Add the savings account to a branch
branch1.add_account(savings_account)
Checking Account
A checking account can be created using the CheckingAccount class. It requires an account number, account holder's name, and initial balance:

python
Copy code
from account import CheckingAccount

# Create a checking account
checking_account = CheckingAccount(account_number="987654321", account_holder="Jane Doe", balance=500)

# Add the checking account to a branch
branch2.add_account(checking_account)
Loan Account
A loan account can be created using the LoanAccount class. It requires an account number, account holder's name, initial balance, and loan amount:

python
Copy code
from loan import LoanAccount

# Create a loan account
loan_account = LoanAccount(account_number="1122334455", account_holder="Alice", balance=0, loan_amount=10000)

# Add the loan account to a branch
branch1.add_account(loan_account)
Reward Accounts
Reward accounts combine the features of savings or checking accounts with a reward points system. They can be created using the RewardSavingsAccount and RewardCheckingAccount classes:

python
Copy code
from enhanced_bank import RewardSavingsAccount, RewardCheckingAccount

# Create a reward savings account
reward_savings_account = RewardSavingsAccount(account_number="123123123", account_holder="Bob", balance=2000, interest_rate=0.03, reward_points=100)

# Create a reward checking account
reward_checking_account = RewardCheckingAccount(account_number="321321321", account_holder="Charlie", balance=1000, reward_points=50)

# Add the reward accounts to branches
branch2.add_account(reward_savings_account)
branch1.add_account(reward_checking_account)
Performing Operations on Accounts
Deposit
To deposit an amount into an account, use the deposit method:

python
Copy code
# Deposit into savings account
savings_account.deposit(500)
Withdraw
To withdraw an amount from an account, use the withdraw method:

python
Copy code
# Withdraw from checking account
checking_account.withdraw(200)
Repay Loan
To repay a loan, use the repay_loan method on a loan account:

python
Copy code
# Repay loan
loan_account.repay_loan(1000)
Earn Rewards
To earn reward points on a reward account, use the earn_rewards method:

python
Copy code
# Earn rewards on reward account
reward_savings_account.earn_rewards(500)
Redeem Rewards
To redeem reward points, use the redeem_rewards method:

python
Copy code
# Redeem rewards on reward account
reward_checking_account.redeem_rewards(20)
Utility Functions
Transfer Funds
To transfer funds from one account to another, use the transfer function:

python
Copy code
from utilities import transfer

# Transfer funds from one account to another
transfer(from_account=savings_account, to_account=checking_account, amount=300)
Logging Operations
The package includes a decorator to log operations performed on accounts. This can be useful for tracking account activity:

python
Copy code
from decorators import log_operation

@log_operation
def custom_operation(account, amount):
    account.deposit(amount)

# Perform custom operation
custom_operation(savings_account, 150)
Database Management
The package uses SQLite to manage account and bank details. All account and bank operations are automatically saved to the database. This ensures that all changes are persistent and can be retrieved later.

Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to submit a Pull Request on GitHub.

License
This project is licensed under the MIT License.
