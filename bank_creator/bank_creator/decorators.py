import functools

# Decorator to log operations performed on the account
def log_operation(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        account = args[0]
        print(f"{func.__name__} called for {account.account_holder}'s account.")
        return result
    return wrapper
