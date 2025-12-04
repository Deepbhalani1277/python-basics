def factorial(n):
    '''calculate the factorial '''
    if (n==0 or n==1):
        return 1
    else:
        return (n * factorial(n-1))

print(factorial(5))

#quick quize
#fibonacci series

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

for i in range(7):
    print(fib(i), end=" ")

print(fib(7))