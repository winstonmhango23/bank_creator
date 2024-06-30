from account import SavingsAccount, CheckingAccount
from loan import LoanAccount
from reward import RewardAccount

# Class combining SavingsAccount and RewardAccount
class RewardSavingsAccount(SavingsAccount, RewardAccount):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.02, reward_points=0):
        SavingsAccount.__init__(self, account_number, account_holder, balance, interest_rate)
        RewardAccount.__init__(self, reward_points)

# Class combining CheckingAccount and RewardAccount
class RewardCheckingAccount(CheckingAccount, RewardAccount):
    def __init__(self, account_number, account_holder, balance=0, reward_points=0):
        CheckingAccount.__init__(self, account_number, account_holder, balance)
        RewardAccount.__init__(self, reward_points)
