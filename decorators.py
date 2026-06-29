def check_balance_decorator(func):
    def wrapper(balance, amount):
        commission = 1
        total_needed = amount + commission
        if balance < total_needed:
            return "error: not enough cash (you need amount + 1)"
        updated_balance_after_commission = balance - commission
        return func(updated_balance_after_commission, amount)
    return wrapper

@check_balance_decorator
def make_transaction(balance, amount):
    
    remaining_balance = balance - amount
    return f"paid succesfully, remaining {remaining_balance} lari"

#example

print(make_transaction(100, 50))





#second homework






import functools

def count_calls(func):
    @functools.wraps(func)  
    def wrapper(*args, **kwargs):
        wrapper.calls += 1  
        print(f"function '{func.__name__}' was called {wrapper.calls} times.")
        return func(*args, **kwargs)
    wrapper.calls = 0  
    return wrapper

@count_calls
def say_hello(name):
    return f"hello, {name}!"
say_hello("giorgi")
say_hello("ani")
say_hello("luka")
print(f"was called {say_hello.calls} times.")