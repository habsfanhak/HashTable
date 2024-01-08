class LinkedList:
    class Node:
        def __init__(self, data, next=None, prev=None):
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
        current_node = self.front
        counter = 0

        while (current_node.next.get_data() is not None):
            current_node = current_node.next
            counter += 1

        return counter
    
    def insert(self, data):
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
    
    def search(self, data):
        current_node = self.front

        while current_node is not self.back:
            if current_node.get_data() is data:
                return current_node
            
            current_node = current_node.get_next()

        return None
    

    


    


        