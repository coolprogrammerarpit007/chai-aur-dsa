class Node:
    def __init__(self,info,next=None):
        self.info = info
        self.next = next
        
        
class SinglyLinkedList:
    def __init__(self,head=None):
        self.head = head
        
    def insertAtStart(self,value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp
        
    def insertAtMiddle(self,value,x):
        temp = Node(value)
        t1 = self.head
        
        while(t1.next != None):
            if(t1.info == x):
                temp.next = t1.next
                t1.next = temp
            t1 = t1.next
            
        
        
    def insertAtEnd(self,value):
        temp = Node(value)
        if(self.head != None):
            t1 = self.head
            while(t1.next != None):
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp
            
    def deleteLL(self,value):
        t1 = self.head
        prev = t1
        
        if(t1.info == value):
            self.head = t1.next
        while(t1.next != None):
            if(t1.info == value):
                prev.next = t1.next
                break
            else:
                prev = t1
                t1 = t1.next
                
        if(t1.info == value):
            prev.next = None
            
    def printLL(self):
        t1 = self.head
        while(t1.next != None):
            print(t1.info)
            t1 = t1.next
        print(t1.info)
            
            
obj = SinglyLinkedList()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtEnd(40)
obj.insertAtEnd(50)
obj.insertAtStart(100)
obj.insertAtStart(101)
obj.insertAtMiddle(786,30)
obj.deleteLL(786)
obj.deleteLL(40)
obj.deleteLL(50)
obj.deleteLL(30)

obj.printLL()