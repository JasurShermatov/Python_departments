class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance


    def deposit(self, amount):
        if amount>0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self,    amount):
        if 0<amount<self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}.")
        else:
            print("Withdrawal amount must be positive and less than the current balance.")

    def get_balance(self):
        return self.__balance


account = BankAccount("Alice", 100000)
print(f"Account owner: {account.owner}")
print(f"Initial balance: {account.get_balance()}")

account.deposit(50000)
account.withdraw(20000)
print(f"Final balance: {account.get_balance()}")

# account.withdraw(1500)  # This should fail
# account.deposit(-100)    # This should also fail





