class GunClip():
    # pass in 2 things
    # java is this. python is self when referring to classes in python
    # __init__ python new class created 
    def __init__(self, capacity):
        self.capacity = capacity
        self.amount = 0

    def reload(self):
        self.amount = self.capacity

    def empty(self):
        self.amount = 0

    def shoot(self, amount):
        self.amount -= amount
        if(self.amount == 0):
            self.amount = 0
            print("empty")
        

glock = GunClip(24)
ruger = GunClip(17)


glock.reload()
glock.empty()
glock.reload()
print(glock.amount)
glock.shoot(15)
print("you have {} rounds left your glock ".format(glock.amount))

ruger.reload()
print(ruger.amount)

glock.reload()
print(f"You have {ruger.amount} rounds left in your ruger.")
print("this is your current rounds left in your clip {}".format(glock.amount))
