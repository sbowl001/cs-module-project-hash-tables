# watch 10 30 - 10:37


my_dict['key1'] = 1 
my_dict['key2'] = 2 
my_dict['key3'] = 3
my_dict['key4'] = 4

{'key2', 'key4', 'key3': 3, "key1"}


d = {
    "foo": 1,
    "bar": 99,
    "qux": 42,
}


# cant sort  a dict, specially not hash tables in general 

# but we could sort a list based on it


for pair in d.items():
    print(pair)

dict_list = list(d.items())

dict_list.sort() 

dict_list.sort(reverse = True) 

# how to sort by value, not by key?
# (x, y) => x + 1

dict_list.sort(key = lambda pair: pair[1])

# sort by descending value , using Python's lambda functions 

dict_list.sort(key = lambda pair: pair[1], reverse= True)