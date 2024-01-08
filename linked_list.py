class LinkedList:
    class Node:
        def __init__(self, data, next=None, prev=None):
            #Initializes the node
            self.data = data
            self.next = next
            self.prev = prev
    
        def get_data(self):
            return self.data
        
        def get_next(self):
            return self.next
        
        def get_prev(self):
            return self.prev
    
    def __init__(self):
        #Initializes sentinel nodes
        self.front = self.Node(None)
        self.back = self.Node(None, None, self.front)
        self.front.next = self.back

    def get_front(self):
        return self.front.next
    
    def get_back(self):
        return self.back.prev
    
    def is_empty(self):
        if self.front.next.get_data() is None:
            return True
        
        return False
    
    def __len__(self):
        #Iterates through linked list to produce len
        current_node = self.front
        counter = 0

        while (current_node.next.get_data() is not None):
            current_node = current_node.next
            counter += 1

        return counter
    
    def insert(self, data):
        #Inserts data in a node at the back of the list
        new_node = None

        if self.is_empty():
            new_node = self.Node(data, self.back, self.front)
            self.front.next = new_node
            self.back.prev = new_node
        else:
            new_node = self.Node(data, self.back, self.back.prev)
            self.back.prev.next = new_node
            self.back.prev = new_node


        return new_node
    
    def search(self, key):
        #Searches the list based on the provided key
        current_node = self.front.next

        while current_node is not self.back:
            node_data = current_node.get_data()

            if node_data[0] == key:
                return current_node
            
            current_node = current_node.get_next()

        return None
    
    def delete(self, key):
        #Searches for the given node, deletes it, and rearranges the list to make for the deleted node's absence
        del_node = self.search(key)

        if del_node is not None:
            del_node.prev.next = del_node.next
            del_node.next.prev = del_node.prev

            del_node.data = None

            del del_node

            return True
        else:
            return False
        
    def clear(self):
        #Clears the linked list and resets the sentinel nodes to point at eachother
        current_node = self.front.next
        temp_node = None

        while current_node is not self.back:
            temp_node = current_node
            current_node = current_node.next

            temp_node.data = None

            del temp_node

        self.front.next = self.back
        self.back.prev = self.front


        
    

    


    


        