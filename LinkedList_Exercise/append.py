class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        

class LinkedList:
    def __init__(self,value=None):
        new_node = Node(value) if value else None
        self.head = new_node if new_node else None
        self.tail = new_node if new_node else None
        
    def is_list_empty(self):
        return self.head is None and self.tail is None
    
    def traverse_through_list(self):
        """ traversing through linked list """
        current_node = self.head
        values = []
        
        while current_node is not None:
            values.append(str(current_node.data))
            current_node = current_node.next
            
        print(" -> ".join(values))
    
    
    def append_item(self,value):
        """ Append New Node at the end of linked list """
        new_node = Node(value)
        if self.is_list_empty():
            self.head = new_node
            self.tail = new_node
            return
            
        current_node = self.head
        
        while current_node.next:
            current_node = current_node.next
            
            
        current_node.next = new_node
        self.tail = new_node
        
        
first_linked_list = LinkedList(25)
first_linked_list.append_item(35)
first_linked_list.append_item(45)
first_linked_list.append_item(55)
first_linked_list.traverse_through_list()