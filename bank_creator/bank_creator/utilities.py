# Function to transfer amount from one account to another
def transfer(from_account, to_account, amount):
    if from_account.balance >= amount:
        from_account.withdraw(amount)
        to_account.deposit(amount)
        print(
            f"Transferred {amount} from {from_account.account_holder} to {to_account.account_holder}."
        )
    else:
        print("Insufficient funds for transfer.")
