class Atm (object):
    def __init__(self,details) :
        self.details = details

    def check(self) :
         return f"Account: {self.name}"

atm_obj = Atm("NAME:ABC, ACCOUNT NUMBER:xyz, PIN:xxxxxx, BALANCE:infinty")
print(atm_obj.details)