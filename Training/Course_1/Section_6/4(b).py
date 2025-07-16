"""
1. Create a class named Book
2. Its properties are name and pages
3. Given two Book objects, we want to add the two objects with the + operator
4. Print the total number of pages for the objects
"""

class Book:
    def __init__(self, name, pages):
        self.name = name
        self.pages = pages
    def __add__(self, other):
        return self.pages+ other.pages

a = Book('12 Rules for life', 250)
b = Book("Dante's Inferno", 650)
print (a+b)