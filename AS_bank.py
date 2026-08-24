class account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print()
            print("welcome to the AS BANK 🙏🏻")
            print(f"Deposited: {amount}. New balance: {self.balance}\n")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print()
            print("welcome to the AS BANK 🙏🏻")
            print(f"Withdrew: {amount}. New balance: {self.balance}\n")
        else:
            print("Invalid withdrawal amount.")

    def display_balance(self):
        print()
        print("welcome to the AS BANK 🙏🏻")
        print(f"for Account Number: {self.account_number}, Balance: {self.balance}\n")

a = account("123456789", 1000)
a.display_balance()
a.deposit(500)
a.withdraw(200)
a.display_balance()
