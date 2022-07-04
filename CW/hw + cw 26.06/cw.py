def yield_check(n):
    for elem in range(n):
        yield elem + 1



def fib(n):
    fib0 = 1
    yield fib0
    
    fib1 = 1
    yield fib1
    
    for i in range(n - 2):
        fib0, fib1 = fib1, fib0 + fib1
        yield fib1
 
 

for num in fib(10):
    pass

print(num)
    
    
