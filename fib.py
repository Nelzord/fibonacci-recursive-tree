#base case: fib(0) => 1
#base case: fib(1) => 0

#rec step: fib(n) = fib(n - 1) + fib(n - 2)

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

#fib function implemented non recursively

def fibnoreclist(n):
    if n == 1:
        return 1
    if n == 2:
        return [1, 1]
    foo = [1, 1]
    for i in range(2, n):
        foo.append(foo[-1] + foo[-2])
    return foo
