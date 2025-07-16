"""
1. The sequence 0, 1, 1, 2, 3, 5, 8, … is known as the Fibonacci sequence.
    Each successive number is found by adding up the two preceding numbers
    We can define the function like this:
    f(n) = f(n-1) + f(n-2), where f(n) represents the nth Fibonacci number and
    f(0) = 0
    f(1) = 1
    
    Write a program, recursively and iteratively, that prints out the nth Fibonacci number.
"""
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else :
        return fibonacci(n-1)+fibonacci(n-2)

num = int(input("Enter the number: "))
print(fibonacci(5))