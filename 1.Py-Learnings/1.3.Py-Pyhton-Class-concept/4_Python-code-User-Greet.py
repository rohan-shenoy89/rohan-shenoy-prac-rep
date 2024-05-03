#Let's create a simple Python class that represents a User. Each user will have attributes for their name, email, and age. We'll also include a method to greet the use

class User():

    def __init__(self,name,email,age):
        self.name = name
        self.email = email
        self.age = age

    def greetUser(self):
       return f"Hello {self.name} I hope you are doing great. You are {self.age} right?"


user1 = User("Rohan",'rs@ssss.com',34)
print(user1.greetUser())
