class employeeaddress:
   def __init__(self,address,pincode):
        self.Address = address
        self.Pcode = pincode
   def getAddresspincode(self):
        return self.Address + self.Pcode
emp2 = employeeaddress("ameerpet hyderabad" , "50002")
var = emp2.getAddresspincode()
print (var)