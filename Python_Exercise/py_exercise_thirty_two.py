class Native:
    def __init__(self, firstname, lastname, phonenumber, payment):
        self.firstname = firstname
        self.lastname = lastname
        self.phonenumber = phonenumber
        self.payment = payment
        self.email = firstname + '_' + lastname + '@semicolon.africa'

    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)

    def phonenumber(self):
        return '{}'.format(self.phonenumber)

    def payment(self):
        return '{}'.format(self.payment)

    def email(self):
        return self.email


native_1 = Native('Precious', 'Lois', '09031111963', 50000, )
native_2 = Native('Olatoye', 'David', '08137271515', 1000000, )
native_3 = Native('Amara', 'David', '09001611962', 30000, )

print(Native.fullname(native_3))
print(Native.payment(native_3))
print(Native.email(native_3))
print(native_3.__dict__) 
