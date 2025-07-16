"""
1. Create a dictionary called contacts
    contacts = {“Alice”: “123-456-7890”, “Bob”: “945-879-1230”, “Carol”, “136-275-2985”}
    Ask the user
    if they want to add a new contact
    Ask for the key, value pair
    Print out the contacts dictionary with the modification
    retrieve the number of an existing contact
    Ask for the name of the person
    Display number
"""
contacts = {'Alice': 123-456-7890, 'Bob': 945-879-1230, 'Carol': 136-275-2985}
ch = 'y'
while ch == 'y' :
    user_input = input("Enter 'yes' to add a new contact: ")
    if user_input == 'yes' :
        key = input("Enter the key: ")
        value = input("Enter the value: ")
        contacts[key] = value
        print(contacts)
    else :
        break
    ch = input("Enter y to continue adding a new contact: ")

sum = 0
for i in contacts:
    sum = sum+1
print("The number of existing contacts: ",sum)

user_input = input("Enter name of a person: ")
print(contacts[user_input])