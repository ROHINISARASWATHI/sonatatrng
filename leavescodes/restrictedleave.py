from leave import leave
class restrictedLeave(leave):
    def _init_(self,employeeid,name,leavebalance,DateofBirth):
        super()._init_(employeeid, name, leavebalance)
        self.dob=DateofBirth
    def ApplyLeave(self):
        return self.name,self.dob
