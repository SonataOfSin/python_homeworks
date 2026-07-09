class BankAccount:
    
    bank_name = "BOG Bank"
    __total_accounts = 0  

    def __init__(self, owner, balance):
        BankAccount.__total_accounts += 1
        self._owner = owner 
        self.__account_number = f"AN{BankAccount.__total_accounts:04d}"
        if BankAccount.validate_amount(balance):
            self.__balance = balance
        else:
            self.__balance = 0
            print(f"Warning: Invalid initial balance for {owner}. Set to 0.")

    def deposit(self, amount):
        if BankAccount.validate_amount(amount):
            self.__balance += amount
            print(f"Successfully deposited {amount} to account {self.__account_number}.")
        else:
            print("Transaction failed: Deposit amount must be positive.")

    def withdraw(self, amount):
        if not BankAccount.validate_amount(amount):
            print("Transaction failed: Withdrawal amount must be positive.")
            return
        
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Successfully withdrew {amount} from account {self.__account_number}.")
        else:
            print("Transaction failed: Insufficient funds.")

    def check_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number
    
    def change_owner(self, new_owner):
        self._owner = new_owner
        print(f"Account owner changed to: {new_owner}")

    @classmethod
    def get_total_accounts(cls):
        return cls.__total_accounts

    @staticmethod
    def validate_amount(amount):
        return amount > 0

    def __str__(self):
        return f"Account: {self.__account_number} | Owner: {self._owner}"


# --- კოდის ტესტირება ---


acc1 = BankAccount("Giorgi Nakashidze", 1000)
acc2 = BankAccount("Nino Beridze", 500)
acc3 = BankAccount("Nika Chighladze", -50)  

print("--- printing objects ---")
print(acc1)
print(acc2)
print(acc3)

print("\n--- operations on nino's account ---")
acc2.deposit(200)
acc2.withdraw(100)
acc2.withdraw(1000)  
print(f"Nino's current balance: {acc2.check_balance()}")

print("\n--- text to change account details ---")

print(f"Acc1 Number: {acc1.get_account_number()}")
acc1.change_owner("Giorgi Chkheidze")
print(acc1)

print("\n--- statistics from the bank ---")

print(f"Bank Name: {BankAccount.bank_name}")
print(f"Total Accounts Created: {BankAccount.get_total_accounts()}")