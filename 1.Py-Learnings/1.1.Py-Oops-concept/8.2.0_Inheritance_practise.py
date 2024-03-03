# Example of Inheritance in python

# The above example is Single level inheritance
class Car:   #Parent/Base class

    @staticmethod
    def start():
        print("Car Started...vroom vroom")

    @staticmethod
    def stop():
        print("Car Stopped...")

class BrandCar(Car):       # Derived/Child Class

    def __init__(self, brand, model, fuel):
        self.brand = brand
        self.model = model
        self.fuel = fuel

car1 = BrandCar("Toyota","L5","Diesel")

print(car1.brand, car1.model, car1.fuel)

# The above example is Multi-level inheritance

class Toyota(BrandCar):

    def __init__(self, name):
        self.name = name


car1 = Toyota("Fortuner")
print(car1.name)
print(car1.start())

# The above example is Multiple inheritance

