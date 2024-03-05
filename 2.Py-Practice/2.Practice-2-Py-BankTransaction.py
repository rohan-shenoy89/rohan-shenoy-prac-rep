class AccDetails:

    @staticmethod
    def bankName():
        return "Welcome to ANZ Bank"

    def __init__(self, Acc_No, Acc_Hldr_Nm, Balance):
        self.Acc_No = Acc_No
        self.Acc_Hldr_Nm = Acc_Hldr_Nm
        self.Balance = Balance

    def account_holder(self):
        if self.Acc_Hldr_Nm != '':
            return f"Hi Mr.{self.Acc_Hldr_Nm}"
        else:
           return "Invalid Name"

    def acc_details(self):
        if len(str(self.Acc_No)) < 8:
            return "Invalid Account Number"
        else:
            return self.Acc_No

    def init_Amount(self):
        if self.Balance < 100:
            return f"LOW BALANCE - {self.Balance}"
        else:
            return f"BALANCE - {self.Balance}"

    def debitAmt(self, Amount):
        self.Balance -= Amount
        print(f"Rs. {Amount} was debited from your account: {self.Acc_No}")
        print("----------------------------------------------------------")
        print(f"BALANCE - {self.Balance}")

    def creditAmt(self, Amount):
        self.Balance += Amount
        print(f"Rs. {Amount} was credited to your account: {self.Acc_No}")
        print("----------------------------------------------------------")
        print(f"BALANCE - {self.Balance}")

p1 = AccDetails(123456789,"Rahul Kumar",10000)
print(p1.bankName())
print("-------------------")
print(p1.account_holder() , '-' , p1.acc_details(),end='\n')
print("-------------------")
print(p1.init_Amount())
print("-------------------\n")
p1.debitAmt(100)
print("-------------------\n")
p1.creditAmt(1250)

