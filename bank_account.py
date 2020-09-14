# class Bank_Account():
#     def __init__(self, checking, saving):
#         self.checking = checking
#         self.saving = saving
#         self.amount = 0
class BankAccount():
    def __init__(self, kind, pin):
        self.kind = kind
        self.balance = 0
        self.overdraft_fees = 0
        self.pin = pin

    def deposit(self, amount):
        self.balance += amount

    def withdrawl(self, amount, pin_from_user):
        if (self.pin == pin_from_user):
            if(self.balance < amount):
                print("Sorry, you dont have that amount in your accont.")
                return
            elif(self.balance == amount):
                self.balance -= amount
                print("You are now emmpty my friend aka you're broke")
            else:
                self.balance -= amount
                print("Current balance is now {}".format(self.balance")
        else: 
            print("The pin number is incorrect. Please try again")


        # if (self.balance < 0):
        #     self.overdraft_fees += 36
        # return amount

    def change_pin(self, pin):
        self.pin=pin
        print(f"The new pin number is {self.pin}")


channee_checking=BankAccount("checking", 1234)
print("My new account is a {} account ".format(channee_checking.kind))

channee_checking.deposit(3000)
# print("My current balance is ${}.".format(channee_checking.balance))

channee_checking.withdrawl(1500, 1555)
# print("My current balance is ${}.".format(channee_checking.balance))

channee_checking.withdrawl(2000, 1234)
# print("My overdraft fee is currently {} ".format(
channee_checking.overdraft_fees))

channee_checking.change_pin(9987)
