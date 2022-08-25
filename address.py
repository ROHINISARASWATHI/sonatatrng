class employeeaddress:
   def __init__(self,address,pincode):
        self.Address = address
        self.Pcode = pincode
   def getAddresspincode(self):
        return self.Address + self.Pcode
emp2 = employeeaddress("23-16-21/2 Lalithanagar 5th street Rajahmundry Andhrapradesh", "533101")
var = emp2.getAddresspincode()
print (var)