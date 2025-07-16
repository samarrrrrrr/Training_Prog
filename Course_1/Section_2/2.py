for i in range(1,11):
    if i % 3 == 0:
        continue
    print(i)

print("\nNext\n")

i = 0
while i <= 10 :
    if i % 2 == 0:
        i = i+1
        continue
    print(i)
    i = i+1
