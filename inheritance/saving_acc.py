from bank_acc import BankAccount

class SavingAccount(BankAccount):
    def __init__(self, account_holder, balance=0,interest_rate = 0.02):
        super().__init__(account_holder, balance)
        self.__interest_rate = interest_rate

    def add_interest(self):
        interest = self._BankAccount__account_balance * self.__interest_rate
        self._BankAccount__account_balance += interest
        print(f"Interest added : ${round(interest,2)}. New balance : ${round(self._BankAccount__account_balance,2)}")

savings = SavingAccount("kevin",10000)
savings.deposit(5000)
savings.add_interest()
# savings.add_interest()
# savings.add_interest()
# savings.add_interest()
savings.display_balance()