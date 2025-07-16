"""lst = ["apple", "Banana", "pens", "knife", "book"]

for i in lst :
    print(i)
    if i == 'pens':
        print(True)
        #break"""

string = ''
while True :
    user_input = input("Enter :" )
    if user_input == 'quit':
        print(string)
        break
    string = string + user_input