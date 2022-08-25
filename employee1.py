class employee:
     def __init__(self,firstname,lastname,address,pincode):
        self.fname = firstname
        self.lname = lastname
        self.address = address
        self.pincode = pincode
     def getFullname(self):
         return self.fname[0] + self.lname[0] + self.address + self.pincode

emp1 = employee("Rohini", "Golla","23-16-21/2 Lalithanagar 5th street Rajahmundry Andhrapradesh" , "533101")
fullname= emp1.getFullname()
print(fullname)



