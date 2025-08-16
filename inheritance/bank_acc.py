class BankAccount():
    def __init__(self,account_holder,balance = 0):
        self.__account_holder = account_holder
        self.__account_balance = balance

    def deposit(self,amount):
        self.__account_balance += amount
        print(f"Deposited ${amount}. New balance ${self.__account_balance}")
    
    def withdrawl(self,amount):
        if amount > self.__account_balance:
            print("Insufficient funds")
        else:
            self.__account_balance -= amount
            print(f"Withdrew ${amount}. New balance ${self.__account_balance}")
    
    def display_balance(self):
        print(f"{self.__account_holder}'s balance is ${self.__account_balance}")