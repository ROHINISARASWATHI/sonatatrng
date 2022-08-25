class leave:
    def _init_(self,employeeid,name,leaveBalance):
        self.id=employeeid
        self.name=name
        self.lvbal=leaveBalance
    def applyLeave(self):
        return self.id,self.name,self.lvbal
