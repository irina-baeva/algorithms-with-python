"""Implement a function recursively to get the desired Fibonacci sequence value."""
#  O(2^n) complexity

def get_fib(position):
    if position == 0:
        return 0
    elif position == 1:
        return 1
    else:
        return get_fib(position - 1) + get_fib(position - 2)


print(get_fib(9)) #34
print(get_fib(11)) #89
print(get_fib(0)) #0
print(get_fib(1)) #1

