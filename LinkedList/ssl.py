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
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
        
    def traverse_through_list(self):
        """ Traversing Through NodeList """
        current_node = self.head
        values = []
        
        while current_node:
            values.append(str(current_node.data))
            current_node = current_node.next
            
        print(" -> " . join(values))
        
        
    def append_at_start(self,value):
        """ appending node at the start """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.tail = new_node
        self.length += 1
        
        
    def append_at_end(self,value):
        """ appending item at the end of list """
        new_node = Node(value)
        
        # checking if the list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
            
        current_node.next = new_node
        self.length += 1
        
    def insert_node(self,target_value,new_value):
        """ inserting new node after the target node """
        new_node = Node(new_value)
        
        current_node = self.head
        
        while current_node and current_node.data != target_value:
            current_node = current_node.next
            
        if current_node is None:
            print(f"{target_value} doesn't find so {new_value} could not be added into linked list!")
            return
        
        new_node.next = current_node.next
        current_node.next = new_node
        self.tail = new_node
        self.length += 1
        
    def remove_node(self,target_value):
        """ remove target node from the node list """
        
        if self.head is None:
            print(f"List is empty so no {target_value} value to be removed!")
            return
        
        if self.head.data == target_value:
            self.head = None
            self.tail = None
            self.length = 0
            return
        
        current_item = self.head
        
        while current_item.next and current_item.next.data != target_value:
            current_item = current_item.next
            
            
        current_item.next = current_item.next.next
        self.tail = current_item
        self.length -= 1
        
    
    def search_node_item(self,target_value):
        """ search node through node list """
        index_pos = 0
        
        if self.head is None:
            print(f"Linked List is empty so no value found! ")
            return -1
        
        if self.head.data == target_value:
            print(f"{target_value} found at first position")
            return index_pos
        
        
        
        current_node = self.head
        
        while current_node and current_node.data != target_value:
            index_pos += 1
            current_node = current_node.next
            
            
        if current_node is None:
            print(f"{target_value} not found!")
            return -1
        
        else:
            print(f"{target_value} found at {index_pos} index position")
            return
        
        
            
            
        
        
l1= LinkedList(25)
l1.append_at_end(35)
l1.append_at_end(75)
l1.insert_node(75,105)
l1.append_at_end(55)
l1.append_at_start(10)
l1.insert_node(25,30)
l1.remove_node(30)
l1.search_node_item(55)
l1.traverse_through_list()
            
        