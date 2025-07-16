class Vehicle:
    def __init__(self):
        print("This is a Vehicle")
    def haswheels(self):
        return True

class Car(Vehicle):
    def __init__(self, model):
        super().__init__()
        self.model = model
        print("This is a Car")
    def haswheels(self):
        super().haswheels()
        print ("It has Four Wheels")

Audi = Car(2013)