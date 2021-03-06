class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        # self.items_stored = 0 
        self.hashlist = [None] * capacity 
        self.number_items = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        # items = f'# {self.items_stored}/{self.capacity} items stored'

        # contents = "\n".join([str(index) + " :" + str(linked_list) for index, linked_list in enumerate(self.storage)])

        # return items + contents 
        # return items 

        return self.capacity
    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """

        return self.number_items / self.capacity
        # Your code here
# to do

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # The FNV_offset_basis is the 64-bit FNV offset basis value: 14695981039346656037 (in hex, 0xcbf29ce484222325).
        # The FNV_prime is the 64-bit FNV prime value: 1099511628211 (in hex, 0x100000001b3).
        # Algorithm:
        # hash := FNV_offset_basis do
        # for each byte_of_data to be hashed
        #     hash := hash × FNV_prime
        #     hash := hash XOR byte_of_data
        # return hash 
       
        FNV_offset_basis = 14695981039346656037 
        FNV_prime = 1099511628211 
        hashed_key = FNV_offset_basis
        byte_keys = key.encode()


        for byte in byte_keys:
            hashed_key = hashed_key * FNV_prime
            hashed_key = hashed_key ^ byte 
        return hashed_key

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here

        # key_bytes = key.encode()
        # hash = 5381 
        # for k_byte in key_bytes:
        #     hash = hash * 33 + k_byte 
        #     hash &= 0xffffffff
        # return hash 
        hash = 5381 
        for l in key: 
            hash = ((hash << 5) + hash) + ordl(l)
        return hash 

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here

        # i = self.hash_index(key)
        # self.storage[i] = value

        index = self.hash_index(key)
        # check the index, if it's empty , put a node there
        if self.hashlist[index] is None: 
            self.hashlist[index] = HashTableEntry(key, value)
            self.number_items += 1 
        # otherwise iterate through the linked list 
        else: 
            current_node = self.hashlist[index]
            while current_node is not None: 
                if current_node.key == key: 
                    current_node.value = value 
                    break 
        # check for the key, update value if it's there
        # if we reach the end , add a new node 
                elif current_node.next == None: 
                    current_node.next = HashTableEntry(key, value)
                    self.number_items += 1 
                    break 
                else: 
                    current_node = current_node.next 

# modify put get and delete 
    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        i = self.hash_index(key)
        self.storage[i] = None 


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        i = self.hash_index(key)
        return self.storage[i]


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # print("resize before", self.capacity)

        # new = [None] * new_capacity

        # counter = 0 
        # for item in self.array: 
        #     new[counter] = item 
        #     counter += 1
        # self.array = new 
        # print("resize after", new_capacity)


        # save our old storage

        old_storage = self.hashlist


        # make a new, bigger storage
        self.hashlist = [None] * new_capacity
        self.capacity = new_capacity 

        # iterate through our hashlist 
        for bucket in old_storage: 
            while bucket is not None: 
                # hash key, value
                key = bucket.key 
                value = bucket.value 
                self.put(key, value)
                # key 
                bucket = bucket.next 
                # go on to the next node
        # iterate through every linked list 


# todo

if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
