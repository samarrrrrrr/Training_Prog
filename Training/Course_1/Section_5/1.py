def recursive_sum(n):
    if n == 1:
        return 1
    return n + recursive_sum(n-1)

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print(recursive_sum(7))
print(fact(7))