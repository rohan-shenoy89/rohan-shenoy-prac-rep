# Class Method

class Person:
    name = "Anonymous"

    @classmethod  # Decorator to access and change the class level attribute values

    def changeName(cls, name):
        cls.name = name


p1 = Person()
p1.changeName("Rohan Shenoy")
print(Person.name)
