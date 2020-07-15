

def slow_fibonacci(n):
    if n <= 1: 
        return n 
    return fibonacci(n - 1) + fibonacci(n - 2)



print(fibonacci(8))

print(fibonacci(9))

# Rewatch 9:30 - 9:57


cache = {}
def fibonacci(n):
    if n <= 1:
        return n 

    if n not in cache: 
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return cache[n]


