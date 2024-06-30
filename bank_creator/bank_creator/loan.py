from account import BankAccount
from decorators import log_operation

# Class representing a loan account
class LoanAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0, loan_amount=0):
        super().__init__(account_number, account_holder, balance)
        self.loan_amount = loan_amount  # Loan amount for the account

    def account_type(self):
        return "Loan"

    @log_operation
    def repay_loan(self, amount):
        # Method to repay the loan
        self.loan_amount -= amount
        self.save()  # Save account details to the database
        print(f"Loan repaid {amount}. Remaining loan amount is {self.loan_amount}.")
