class Person:

    def __init__(self, name):
        self.name = name

    def __hello(self):            #This is the private method and cannot be called outside the class.
        print("Hello",self.name)

    def welcome(self):            #This private method can be called in other method and its values can be accessed.
        self.__hello()

p2 = Person("Rohan")
print(p2.welcome())
