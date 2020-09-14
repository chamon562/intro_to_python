class CoffeeCup():
    # pass in 2 things
    # java is this. python is self when referring to classes in python
    # __init__ python new class created 
    def __init__(self, capacity):
        self.capacity = capacity
        self.amount = 0

    def fill(self):
        self.amount = self.capacity

    def empty(self):
        self.amount = 0

    def drink(self, amount):
        self.amount -= amount
        if(self.amount == 0):
            self.amount = 0
            print("Coffee cupt is now empty")
