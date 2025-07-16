"""
1. Create a class named Person
2. Its properties are name and age (initialize the value using the constructor)
3. Create a method, greeting, which will display the name and age properties
4. Create an instance of the Person class
5. Call the method created of the class
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print("Name is ", self.name)
        print("Age is ", self.age)
    
a = Person('Samar', 21)
a.greeting()