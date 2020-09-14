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

# class Android pass in Phone taking everything from the Phone class and use it in the Android class
class Android(Phone):
    def __init__(self, phone_number):
        # super goes up and grabs the phone number attribute from the first class Phone
        super().__init__(phone_number)
        self.keyboard = "Default"
    # after class is defined here say Android.origin
    def __str__(self):
        return "This phone is owned by {}".format(self.number)
        
    def set_keyboard(self, new_keyboard):
        self.keyboard = new_keyboard

Android.ORIGIN = Android("")
hanzo_phone = Android(562888888)
hanzo_phone.set_keyboard("Dvorak")
hanzo_phone.call(818999991)
hanzo_phone.open_app("Google Play Store")

print(hanzo_phone)
