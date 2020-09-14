class Phone():
    def __init__(self, phone_number):
        self.number = phone_number

    # make 2 methods call method and text method
    # call self gives me access to this.self
    def call(self, other_number):
        print("Calling {} from {}".format(other_number, self.number))

    def text(self, other_number, msg):
        print("Sending text to {} from {} ".format(other_number, self.number))
    
    def open_app(self, app_name):
        print("Opening {} on device.".format(app_name))

# pass in phone something you want to inherit
# if you forgot your semi colon: it wont indent autmotically be aware
class IPhone(Phone):
    def __init__(self, phone_number):
        super().__init__(phone_number)
        self.fingerprint = None
    def set_fingerprint(self, new_fingerprint):
        self.fingerprint = new_fingerprint
        # make it a defualt value fingerprint 
    def unlock(self, fingerprint=None):
        if(fingerprint == None  and self.fingerprint == None):
            print("Phone is unlocked because no fingerprint is currently set")
        if(fingerprint == self.fingerprint):
            print("Phone is unlocked")
        else:
            print("Phone locked. Fingerprint does not match")

channee_iphone = IPhone(885999999)
print("Channee Number is {}".format(channee_iphone.number))

channee_iphone.set_fingerprint("password")
print("fingerprint is {}".format(channee_iphone.fingerprint) )

channee_iphone.unlock("password123")

channee_iphone.call(562888888)

channee_iphone.open_app("FaceBook")