class Calculator():
    def add(self,a,b):
        return a + b

    def sub(self,a,b):
        return a - b

    def mul(self,a,b):
        return a * b

    def div(self,a,b):
        if a == 0 | b == 0:
            return "ERROR: Cannot divide by 0"
        else:
            return a / b


calculator = Calculator()
print("""Select the choice: 1 - Add, 2 - Sub, 3 - Mul & 4 - Div """)
choice = int(input("Enter your choice: "))

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if choice == 1:
    print("Result:", calculator.add(num1,num2))
elif choice == 2:
    print("Result:", calculator.sub(num1,num2))
elif choice == 3:
    print("Result:", calculator.mul(num1,num2))
elif choice == 4:
    print("Result:", calculator.div(num1,num2))
else:
    print("Invalid Entry")
