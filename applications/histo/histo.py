# Your code here

with open("robin.txt") as f:
    words = f.read()
    split_words = words.split()


cache = {} 


for word in split_words: 
    if word not in cache: 
        cache[word] = '#'
    else: 
        cache[word] += '#'

items = list(cache.items())

items.sort(key = lambda x: x[1], reverse= True)


for key, value in items: 
    print(f'{key: <18} {value}')