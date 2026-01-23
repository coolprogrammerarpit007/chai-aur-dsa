class Node:
    def __init__(self,value):
        self.data = value
        self.next_node = None
        
        
class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    
    def is_list_empty(self):
        return self.head is None
    
    def traverse_through_all(self):
        elements = []
        current_node = self.head
        
        while current_node:
            elements.append(str(current_node.data))
            current_node = current_node.next_node
            
            
        print(" -> ".join(elements))
        
    def append_node(self,value):
        """ append item at the end """
        new_node = Node(value)
        
        if self.is_list_empty():
            self.head = new_node
            self.tail = new_node
            
            
        else:
            self.tail.next_node = new_node
            self.tail = new_node
            
        self.length += 1
    
    def remove_node(self,target_value):
        """ remove node from the linked-list """
        
        if self.is_list_empty():
            print(f"List is empty no item can be removed....")
            return
        
        
        # if head is target-data to be removed
        if self.head.data == target_value:
            self.head = self.head.next_node
            self.length -= 1
            return
        
        current_node = self.head
        
        while current_node and current_node.next_node.data != target_value:
            current_node = current_node.next_node
            
            
        if current_node is None:
            print(f"{target_value} is not found in the list to be removed!")
            return
        
        current_node.next_node = current_node.next_node.next_node
        self.length -= 1
    
        
        
        
l1 = LinkedList(25)
l1.is_list_empty()
l1.append_node(35)
l1.append_node(45)
l1.append_node(55)
l1.remove_node(45)
l1.remove_node(25)
l1.remove_node(55)
l1.remove_node(35)
l1.traverse_through_all()