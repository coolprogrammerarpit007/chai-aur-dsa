# Linked List:- Linked lists are the linear data-structure where elements are stored in nodes. and each node points to the next node in the sequence. These lists are different from the built-in data-structure as they are not stored in the continuous memory locations.

# we can think linked lists as treasure hints where each clue points to the location of the next clue without the possibility of the skip ahead


# There are two type of linked Lists
# 1. Singly Linked List
# 2. Doubly Linked List

# a.) Singly Linked List:- There are two types of linked lists. The first one, the singly linked list, has nodes that point only to the next node in the sequence. Unlike Python’s built-in lists (contiguous memory), linked list elements can be scattered throughout memory, with each node storing data plus one reference (~8 bytes overhead per node). A singly linked list is simpler to implement but only allows forward traversal. 

#  Implementation of Singly Linked List



class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def is_list_empty(self):
        """ Check if linked list is empty or not """
        return self.head is None
    
    def traverse_through_all(self):
        """ Display all items inside list """
        current_item = self.head
        values = []
        
        while current_item:
            values.append(str(current_item.data))
            current_item = current_item.next
            
            
        print(" -> ".join(values))
        
    def insert_at_start(self,value):
        """ Insert New Node at starting Position """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        
    def insert_at_end(self,value):
        """" Insert element at the end of linked list """
        new_node = Node(value)
        
        # Handle empty list case first
        if self.is_list_empty():
            self.head = new_node
            return 
        
        current_element = self.head
        
        while current_element.next:
            current_element = current_element.next
            
        current_element.next = new_node
        
    def insert_at_middle(self,target_value,new_value):
        """ Add a new element after node containing the target value """
        current_item = self.head
        
        if self.is_list_empty():
            return
        
        while current_item and current_item.data != target_value:
            current_item = current_item.next
            
        if current_item is None:
            print(f"{target_value} is not found! ")
            return
        
        new_node = Node(new_value)
        new_node.next = current_item.next
        current_item.next = new_node
        
        
    def remove_value(self,target_value):
        """ Remove the target node value """
        
        if self.is_list_empty():
            print(f"{target_value} can not be deleted as list is empty")
            return
        
        if self.head.data == target_value:
            self.head = self.head.next
            return
        
        current_item = self.head
        
        while current_item.next and current_item.next.data != target_value:
            current_item = current_item.next
            
        if current_item is None:
            print(f"{target_value} is not found! ")
            return
        
        current_item.next = current_item.next.next
        
        
    def search_item(self,target_value):
        """ Search Item through the Linked List """
        current_item = self.head
        count = 0
        while current_item and current_item.data != target_value:
            current_item = current_item.next
            count += 1
            
        if current_item is None:
            print(f"{target_value} is not found! ")
            return
        
        print(f"{target_value} found at position: {count}")
        
        
            
    
     
l1 = LinkedList()
l1.insert_at_start(20)
l1.insert_at_start(10)
l1.insert_at_end(30)
l1.insert_at_end(40)
l1.insert_at_middle(30,55)
l1.insert_at_middle(55,65)  
l1.insert_at_middle(40,73)
l1.remove_value(55)  
l1.remove_value(65)  
l1.remove_value(73)  
l1.traverse_through_all()
l1.search_item(95)