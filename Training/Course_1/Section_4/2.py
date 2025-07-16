myfile = open("2.txt", "r")
print(myfile.read())
myfile.close()

myfile = open("2.txt", "r")
print(myfile.read(5))
myfile.close()

myfile = open("2.txt", "r")
print(myfile.read(5))
print(myfile.read(5))
myfile.close()

myfile = open("2.txt", "r")
print(myfile.read(5))
myfile.seek(0)
print(myfile.read(5))
myfile.close()

myfile = open("2(a).txt", "w")
myfile.write("Hello, This is write operation")
myfile.write("Hello, This is write operation")
myfile.close()

myfile = open("2(a).txt", "a")
myfile.write("Hello, This is write operation")
myfile.write("Hello, This is write operation")
myfile.close()