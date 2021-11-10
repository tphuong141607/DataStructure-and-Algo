# Implementing Hash Table
# Handling collisions (we do Option 1)
    #   Option1: Linked Lists = Each spot in the array is an array of tuple (key, value)
    #   Option2: Probing = find an empty spot to store the (key, value). Each spot in the array is a tuple

class HashTable: 
    # 1. The Hash Table is an array of length 100
    def __init__(self):
        self.LENGTH = 10 
        self.arr = [[] for i in range(self.LENGTH)]

    # 2. Hash Function: O(len(key))
    #   a. Convert each string char to its corresponding ASCII Decimal Code (using function ord(ch))
    #   b. Sum all ASCII Decimal Code
    #   c. Mod(sum, arrLen) -- The reminder is always less than the divisor
    def get_hash(self, key):
        hash = 0
        for char in key: 
            hash += ord(char) 
        return hash % self.LENGTH 

    # 3. Add the key-vale pair to our hash table: O(len(key))
    def add(self, key, val): 
        hash = self.get_hash(key)
        found = False
        # Add a new (key, value) to the linked list
        # If key already exists, update the value
        for idx, atuple in enumerate(self.arr[hash]): 
            # key exists
            if len(atuple) == 2 and atuple[0]==key: 
                self.arr[hash][idx] = (key, val)
                found = True
                break

        # key NOT exist
        if not found: 
            self.arr[hash].append((key, val))
    
    def __setitem__(self, key, val):  # Allow us to access value using arr[key]
        self.add(key, val)

    # 4. Get the value, given a key O(len(key))
    def get(self, key): 
        hash = self.get_hash(key)
        for atuple in self.arr[hash]:
            if atuple[0] == key: 
                return atuple[1]

    def __getitem__(self, key): # Allow us to access value using arr[key]
        return self.get(key)

    # 5. Delete a key-value pair by key 
    def delete(self, key): 
        hash = self.get_hash(key)
        for idx, atuple in enumerate(self.arr[hash]):
            if atuple[0] == key: 
                self.arr[hash].pop(idx)

    def __delitem__(self, key): # Allow us to access value using arr[key]
        self.delete(key)

    
my_ht = HashTable()
my_ht["march 17"] = 120
my_ht["march 6"] = 120
print(*my_ht.arr, sep='\n')


