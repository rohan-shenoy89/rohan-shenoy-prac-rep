# The above example is Multiple inheritance

class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to class B"

class C(A, B):                  # Here the class C is inheriting the properties of Class A and B
    varC = "Welcome to class C"

c1 = C()

print(c1.varA)
print(c1.varB)
print(c1.varC)
