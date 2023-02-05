# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:
    # Constructor
    def __init__(self_ebs, name_ebs, email_ebs, age_ebs):
        self_ebs.name = name_ebs
        self_ebs.email = email_ebs
        self_ebs.age =age_ebs


    def greeting(self_ebs):
        return f'My name is {self_ebs.name} and I am {self_ebs.age}'

    def has_birthday(self_ebs):
        self_ebs.age += 1

# Extend class
class Customer(User):
    #Constructor
    def __init__(self_ebs, name_ebs, email_ebs, age_ebs):
        self_ebs.name = name_ebs
        self_ebs.email =email_ebs
        self_ebs.age = age_ebs
        self_ebs.balence = 0

    def set_balance(self_ebs, balance_ebs):
        self_ebs.balence = balance_ebs

    def greeting(self_ebs):
        return f'My name is {self_ebs.name} and I am {self_ebs.age} and my balence is {self_ebs.balence}'

# Init user object
giorno = User('Giorno Giovana', 'giorno@gmail.com', 37)
# Init customer object
joseph = Customer('Joseph Joestar', 'joseph@yahoo.com', 25)

joseph.set_balance(500)
print(joseph.greeting())

giorno.has_birthday()
print(giorno.greeting())
