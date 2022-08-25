from leave import leave
class basketofleave(leave):
    def _init_(self,employeeid,name,LeaveBalance,ReasonForApplyingLeave):
        super().__init__(employeeid,name,LeaveBalance)
        self.reason=ReasonForApplyingLeave
    def applyLeave(self):
        return str(self.Id)+self.name+ self.reason.upper()
