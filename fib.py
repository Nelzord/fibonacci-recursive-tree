#base case: fib(0) => 1
#base case: fib(1) => 0

#rec step: fib(n) = fib(n - 1) + fib(n - 2)

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

