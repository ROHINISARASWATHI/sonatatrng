class Account:
    def __init__(self,accnum,name,type,balance):
        self.accountnumber = accnum
        self.Name = name
        self.Type = type
        self.blc=balance
    def details(self):
        return self.accountnumber + self.Name + self.Type + self.blc
