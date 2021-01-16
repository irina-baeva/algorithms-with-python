# Find factorial of n or n!
# If n = 0, then n! = 1
# If n > 0, then n! = n*(n-1)!

def factorial(n):
    if n == 0:
        return 1
    else:
        print(n)
        return n * factorial(n - 1)


factorial_3 = factorial(3)
print(factorial_3) #6

