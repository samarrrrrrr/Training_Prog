mydict = {'apple' : 1, "banana" : 2, "grape" : 2}
print(type(mydict))
print(mydict)

mydict = {}
mydict['apple'] = 1
mydict['banana'] = 2
mydict['grape'] = 3
print(mydict)

del mydict['apple']
print(mydict)

#print(mydict['banana'])
mydict = {'apple' : 1, "banana" : 2, "grape" : 3}
for i in mydict:
    print(i)

for i in mydict.keys():
    print(i)

for i in mydict.values():
    print(i)



price = {'apple' : 25, 'banana' : 20, 'grape' : 2.5}
cart = {'apple' : 4, 'banana' : 12, 'grape' : 20}
total_cost = 0
for i in cart.keys():
    total_cost = cart[i]*price[i] + total_cost
print(total_cost)
