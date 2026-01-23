# Doubly Linked List:- doubly linked list are bi-directional means every node has two pointers next and prev. but the size of node will be 16 bytes compared to 8 bytes. 


class doublyNode:
    def __init__(self,value):
        self.data = value
        self.next_node = None # References to next_node
        self.prev_node = None # References to the previous node


class BidirectionalLinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None
        
        
    def is_empty_list(self):
        """ check if the list is empty or not! """
        return self.head_node is None
    
    def show_forward(self):
        """ show all elements from head to tail """
        elements = []
        current_element = self.head_node
        
        while current_element:
            elements.append(str(current_element.data))
            current_element = current_element.next_node
            
        print(" <--> ".join(elements))
        
        
    def show_backward(self):
        """ show all elements from tail to head """
        elements = []
        current_element = self.tail_node
        
        while current_element:
            elements.append(str(current_element.data))
            current_element = current_element.prev_node
            
        print(" <--> ".join(elements))
        
        
    def add_at_end(self,value):
        """ add new node at the end of node list """
        
        new_node = doublyNode(value)
        
        if self.is_empty_list():
            self.head_node = new_node
            self.tail_node = new_node
            return
        
        # connect the new node at the end
        self.tail_node.next_node = new_node
        new_node.prev_node = self.tail_node
        self.tail_node = new_node
        
        
    def add_at_begin(self,value):
        """ add new node at the beginning of node list """
        
        new_node = doublyNode(value)
        
        if self.is_empty_list():
            self.head_node = new_node
            self.tail_node = new_node
            return
        
        # connecting the new node at the beginning
        self.head_node.prev_node = new_node
        new_node.next_node = self.head_node
        self.head_node = new_node
        
    def remove_node(self,target_value):
        """ remove target node from the bi-directional node list """
        
        if self.is_empty_list():
            print("cannot remove from the empty list!")
            return
        
        current = self.head_node
        
        while current and current.data != target_value:
            current = current.next_node
            
            
        if current is None:
            print(f"{target_value} not found to be removed!")
            return -1
        
        
        # Handle single node first
        
        if self.head_node == self.tail_node:
            self.head_node = None
            self.tail_node = None
            return
        
        # Handle Head Node 
        
        if current == self.head_node:
            self.head_node = current.next_node
            self.head_node.prev_node = None
            return
        
         # Handle tail node removal
        if current == self.tail_node:
            self.tail_node = current.prev_node
            self.tail_node.next_node = None
            return
        
        
        # Handle Middle node removal
        current.prev_node.next_node = current.next_node
        current.next_node.prev_node = current.prev_node
        
