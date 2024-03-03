# Inheritance - Super Method

class Car:   #Parent/Base class

    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car Started...vroom vroom")

    @staticmethod
    def stop():
        print("Car Stopped...")

class BrandCar(Car):       # Derived/Child Class

    def __init__(self, brand, model, fuel, type):
        self.brand = brand
        self.model = model
        self.fuel = fuel
        super().__init__(type)
        super().start()                 # super keyword can be used to access the attributes on parent class.

car1 = BrandCar("Toyota","L5","Diesel","SUV")

print(car1.brand, car1.model, car1.fuel, car1.type)

