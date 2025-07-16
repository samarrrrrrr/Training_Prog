myset = {1,2,3,4,5,6, False, "apple",5.5}
print(myset)
print(type(myset))

myset2 = set()
print(type(myset2))
myset2.add(4.5)
myset2.add(6.5)
myset2.add("apple")
myset2.add("banana")
print(myset2)
myset2.remove(6.5)
myset2.remove("banana")
print(myset2)

set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}

#Union 
print(set1 | set2)

#Intersection 
print(set1 & set2)

#Subtraction 
print(set1 - set2)