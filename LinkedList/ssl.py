# Linked List:- Linked lists are the linear data-structure where elements are stored in nodes. and each node points to the next node in the sequence. These lists are different from the built-in data-structure as they are not stored in the continuous memory locations.

# we can think linked lists as treasure hints where each clue points to the location of the next clue without the possibility of the skip ahead


# There are two type of linked Lists
# 1. Singly Linked List
# 2. Doubly Linked List

# a.) Singly Linked List:- There are two types of linked lists. The first one, the singly linked list, has nodes that point only to the next node in the sequence. Unlike Python’s built-in lists (contiguous memory), linked list elements can be scattered throughout memory, with each node storing data plus one reference (~8 bytes overhead per node). A singly linked list is simpler to implement but only allows forward traversal. 

#  Implementation of Singly Linked List



class ListNode:
    def __init__(self,value):
        self.data = value
        self.next_node = None
        
        
class LinkedList:
    def __init__(self):
        self.first = None
        
        
    #  Method to check is linked list is empty or not
    def is_list_empty(self):
        return self.first is None
    
    # method to traverse through linked list
    
    def show_all_elements(self):
        """ Show all elements in the list """
        current_element = self.first
        values = []
        
        while current_element:
            values.append(str(current_element.data))
            current_element = current_element.next_node

        
        print(" → ".join(values))
        
        
        
    # Inserting elements in the list, it can be at start,end or middle 
    
    def add_to_front(self,value):
        """ Add a new element at the start of the list """
        fresh_node = ListNode(value)
        fresh_node.next_node = self.first
        self.first = fresh_node
        
    def add_to_end(self,value):
        """ Add element at the end of list """
        fresh_node = ListNode(value)
        
        # Handle if list is empty
        if self.is_list_empty():
            self.first = fresh_node
            return
        
        # Navigate to the last element
        current_element = self.first
        while current_element.next_node:
            current_element = current_element.next_node
            
        # connect new node at the end
        current_element.next_node = fresh_node
        
    def add_after_value(self,target_value,new_value):
        " Add a new element after node containing the target value "
        
        # Locate the target node
        current_node = self.first
        
        while current_node and current_node.data != target_value:
            current_node = current_node.next_node
            
        # Handle case where target was not found
        
        if current_node is None:
            print(f"{target_value} is not found!")
            return 
        
        # create and insert new node
        new_node = ListNode(new_value)
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node
        
    


ll = LinkedList()


#  manually inserting for now

n1 = ListNode(25)
n2 = ListNode(35)
n3 = ListNode(45)
n4 = ListNode(55)
n5 = ListNode(65)


ll.first = n1  # linked list now starts at n1
n1.next_node = n2
n2.next_node = n3
n3.next_node = n4
n4.next_node = n5


ll.show_all_elements()