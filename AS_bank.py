class account:

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print()
            print(f"Deposited: {amount}. New balance: {self.balance}\n")
            self.transactions.append(("deposit", amount))
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if self.balance >= 100:
            if 0 < amount <= self.balance:
                self.balance -= amount
                print()
                print(f"Withdrew: {amount}. New balance: {self.balance}\n")
                self.transactions.append(("withdraw", amount))
            else:
                print("Invalid withdrawal amount.")
        else:
            print(f"your bank balance is {self.balance} cannot withdraw amount ")
            print("Balance should be 100 or more")

    def display_balance(self):
        print()
        print(f"for Account Number: {self.account_number}, Balance: {self.balance}\n")

class bank(account):
    def __init__(self,account_number, balance, intrest_rate,status,intrest_balance=0):
        super().__init__(account_number, balance)
        self.intrest_rate = intrest_rate
        self.status = status
        self._intrest_balance = intrest_balance

    def calculate_intrest(self):
        intrest = self.balance * (self.intrest_rate / 100)
        print(f"intrest for Account Number: {self.account_number} at the rate of {self.intrest_rate}% is: {intrest}\n")
        return intrest

    @property
    def intrest_balance(self):
        self.balance += self.balance * (self.intrest_rate / 100)
        return f"balance after intrest is : {self.balance}"

    @property
    def bank_status(self):
        return f"bank status is : {self.status}"
    
user_acc = bank("123456789", 1000, 5, "active")
while True:
    print("=== Welcome to AS BANK ===")
    print("1 : Deposit")
    print("2 : Withdraw")
    print("3 : Know interest rate calculation")
    print("4 : Apply interest & check new balance")
    print("5 : Account status")
    print("6 : Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        amt = float(input("Enter deposit amount: "))
        user_acc.deposit(amt)
    elif choice == "2":
        amt = float(input("Enter withdrawal amount: "))
        user_acc.withdraw(amt)
    elif choice == "3":
        user_acc.calculate_intrest()
    elif choice == "4":
        print(user_acc.intrest_balance)
    elif choice == "5":
        print(user_acc.bank_status)    
    elif choice == "6":
        print("Thank you for using AS BANK!")
        break
    else:
        print("Invalid choice. Try again.\n")
