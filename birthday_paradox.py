# make random keys 
# hash them, and module them 
# keep track of the hashed keys somehow
# stop when we get a collision 


# test out increasing our array size 
import random
import hashlib 

def hash_function(random_key):
    return int(hashlib.sha256(f'{random_key}'.encode()).hexdigest(), 16)


def how_many_before_collision(number_of_buckets):
    tried = set()
    number_tries = 0 
    while True: 
        random_key = random.random()
        hashed_key = hash_function(random_key) % number_of_buckets

        if hashed_key not in tried: 
            tried.add(hashed_key)
            number_tries += 1 
        else: 
            break 

    return number_tries

print(how_many_before_collision(4))
print(how_many_before_collision(8))