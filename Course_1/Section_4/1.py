num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

"""try :
    x = num1/num2
    print (x)
except Exception as e:
    print (e)"""

try :
    x = num1/num2
except Exception as e:
    print (e)
    x = None
finally :
    print(x)
