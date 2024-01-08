from linked_list import LinkedList

class HashTable:
    def __init__(self, cap):
        #Initialize to the passed cap variable
        self.cap = cap
        self.table = [LinkedList() for _ in range(cap)]

    def insert(self, key, data):
        #Hashes the key and inserts the tuple at the produced index
        index = hash(key) % self.cap
        self.table[index].insert((key, data)) 

    def search(self, key):
        #Searches within the indexed list and returns the node
        index = hash(key) % self.cap
        return self.table[index].search(key)
        
    def delete(self, key):
        #Searches within the indexed list and deletes the node
        index = hash(key) % self.cap
        return self.table[index].delete(key)

    def clear(self):
        #Clears all nodes
        for lst in self.table:
            lst.clear()
        