# class Bank_Account():
#     def __init__(self, checking, saving):
#         self.checking = checking
#         self.saving = saving
#         self.amount = 0
class BankAccount():
    def __init__(self, kind):
        self.kind = kind
        self.balance = 0
        self.overdraft_fees = 0
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdrawl(self, amount):
        self.balance -= amount

        if (self.balance <0):
            self.overdraft_fees += 36
        return amount
