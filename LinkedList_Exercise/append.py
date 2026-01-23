class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        
        
class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def is_list_empty(self):
        return self.head is None
    
    
    def traverse_through_all(self):
        """ traverse through list """
        current_item = self.head
        elements = []
        
        while current_item:
            elements.append(str(current_item.data))
            current_item = current_item.next
            
        print(" -> " .join(elements))
        
        
    
    def append_node(self,value):
        """ append item at the end """
        new_node = Node(value)
        
        if self.is_list_empty():
            self.head = new_node
            self.tail = new_node
            
        else:
            self.tail.next = new_node
            self.tail = new_node
            
        self.length += 1
        
        
l1 = LinkedList(15)
# l1.append_node(35)
# l1.append_node(45)
# l1.append_node(55)
l1.traverse_through_all()