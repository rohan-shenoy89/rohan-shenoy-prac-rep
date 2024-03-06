#-----------------------------
# PRACTICE - OOPS
# CORE SUBJECT - Private Class
# DEVELOPER - Rohan Shenoy
#------------------------------

class BankAccount:

    def __init__(self, account_no, account_password, account_balance):
        self.account_no = account_no
        self.__account_password = account_password          # Adding __ before the attribute makes it Private. This will be only visible within the class.
        self.account_balance = account_balance

    # Simple example to mask PII values
    def maskVal(self):
        self.account_no_str = str(self.account_no)
        self.new_account_number = '*' * 4 + self.account_no_str[4:]
        return self.new_account_number

accHolder = BankAccount(123456789,'abde@',11000)
print(accHolder.account_no)
#print(accHolder.account_password)  # --> This will not execute since you are trying to call the private attribute outside the class.
print(accHolder.maskVal())
