"""
1. Create a “student.txt” file, and add three sample names.
    Display the contents of the file to the console
    Take user input to get three more names, and add them to the file.
"""

try :
    myfile = open("student.txt", "w")
    myfile.write("Samar\nAnanya\nAryan")

    myfile = open("student.txt", "r")
    print(myfile.read())
    for _ in range(3):
        Name = str(input("Enter Name: "))
        myfile = open("student.txt", "a")
        myfile.write("\n" + Name)

except Exception as e:
    print(e)
