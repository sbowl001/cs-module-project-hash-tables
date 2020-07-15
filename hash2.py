# big ideas: use all the info you can to scramble stuff, even the bits
## use bit shifting to get a new weird sort-of-random number
def djb2(key):
    hash = 5381
​
    for char in key:
        hash = (( hash << 5) + hash) + ord(char)
        # hash = (( hash * 33) + hash) + ord(char)
    return hash
​
hash_table = [None] * 8
​
​
class HashTableItem:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next
        
​
​
​
def my_hash(s):
    s_utf8 = s.encode()
​
    total = 0
​
    for c in s_utf8:
        total += c
​
    return total
​
def put(key, value):
    hashed_key = my_hash(key)
​
    index = hashed_key % len(hash_table)
​
    # print a warning if we are going to overwrite
    if hash_table[index] != None:
        print('omg think of the data!')
​
    hash_table[index] = HashTableItem(key, value)
​
def get(key):
    hashed_key = my_hash(key)
    index = hashed_key % len(hash_table)
​
    table_item = hash_table[index]
​
    return table_item.value
​
def delete(key):
    hashed_key = my_hash(key)
    index = hashed_key % len(hash_table)
    hash_table[index] = None
​
put("hello", "hello world")
​
put("olleh", "we didnt start the fire")
​
print(get("hello"))
​
print(hash_table)
​
delete("hello")
print(hash_table)
​
# [None, None, None, None, 'hello world', 'we didnt start the fire', None, None]
# [None, None, None, None, None, None, None, None]
​
# open addressing
## put in a surrounding/different index
## linear probing: find the next available index and put it there
# double hashing: hash the hash
# disallow it!
# chaining
​
'''
Index  Chain (linked list)
----   ---------------
0      ("qux", 54)  -> None
1      ("foo", 42)  -> None
2      ("bar", 99)  -> None
3      -> None
4      -> None
​
put("foo", 42)   # hashed to index 1
put("bar", 99)   # hashes to index 2
put("baz", 38)   # hashes to index 1! collision!
put("qux", 54)   # hashes to 0
​
get("qux")
get("foo")
get("fred")  # hashes to 0 --> return None
​
​
delete("baz")
​
'''

# insert a LL into the hash table, when you put something in 
# hash table main data structure : [LL, LL, None, LL , None, None]
# ​how to make the LL work with our hash table?
# ensure each node has a key as well as a value
# change methods to use keys, not just values, where necessary 
# write a method, maybe insert or overwrite
# search for the key, if found, overwrite
# otherwise, None

# generic ListNode and LinkedList
​
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
​
class LinkedList:
    def __init__(self):
        self.head = None
​
    def find(self, value):
        current = self.head
​
        while current is not None:
            if current.value == value:
                return current
        
            current = current.next
​
        return None
​
    def insert_at_tail(self, value):
        node = ListNode(value)
​
        # if there is no head
        if self.head is None:
            self.head = node
        else:
            current = self.head
​
            while current.next is not None:
                current = current.next
            current.next = node
​
    def delete(self, value):
        current = self.head 
        # when deleting the head 

        # if there is nothing to delete
        if current is None:
            return None

        # when deleting the head 
        if current.value == value:
            self.head = current.next 
            return current 
        
        # when deleting something else

        else: 
            previous = current 
            current = current.next 

            while current is not None:
                if current.value == value   #found it !
                    previous.next = current.next  # cut out the current out!
                    return current #return our deleted node 
                else: 
                    previous = current
                    current = current.next 

            return None  #if we got here, nothing was found! 