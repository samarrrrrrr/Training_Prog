class Person :
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("In display Function\n")
        print("I am ", self.name)

t = Person('Samar', 21)
t.display()