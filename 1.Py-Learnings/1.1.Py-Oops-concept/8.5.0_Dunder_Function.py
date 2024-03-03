# Property Method

class Complex:

    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumbers(self):
        print(self.real,"i +", self.img,"j")

    # Dunder Functions in Python
    def __add__(self, num2):
        showReal = self.real + num2.real
        showImg = self.img + num2.img
        print("----------")
        return Complex(showReal, showImg)

c1 = Complex(10,2)
c1.showNumbers()

c2 = Complex(11,3)
c2.showNumbers()

c3 = c1 + c2
c3.showNumbers()
