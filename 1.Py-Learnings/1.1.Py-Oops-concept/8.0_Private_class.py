class Account:

    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass          #This attribute is made private.

    def reset(self):
        print("Show the password: ", self.__acc_pass)   #Since the attribute is private, it cannot be called outside the class.
                                                        #But it can be referred in another method and can be referred from there.

p1 = Account("12345","abcde")
print(p1.acc_no)
print(p1.reset())           # This is where the reset method is called where the PASSWORD can be seen in the output.
