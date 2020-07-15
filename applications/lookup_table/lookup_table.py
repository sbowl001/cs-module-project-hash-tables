# Your code here
import math 
import random 



cache = {}
def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    pairs = (x, y)
    if pairs not in cache: 
        cache[pairs] = slowfun_too_slow(x, y)
    return cache[pairs]
    # Your code here



# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')


# import math 


# lookup_table = {}


# def inverse_root(n):
#     return 1 / math.sqrt(n)


# def populate_lookup_table():
#     for i in range(1, 1000):
#         lookup_table[i] = inverse_root(i)


# populate_lookup_table()