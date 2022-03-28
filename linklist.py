
class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  
 
class LinkedList:
       def __init__(self):
        self.head = None

def push(self, new_data):
 
        new_node = Node(new_data)

        new_node.next = self.head

        self.head = new_node

def append(self, new_data):
        new_node = Node(new_data)
 
        if self.head is None:
            self.head = new_node
            return
 
        last = self.head
        while (last.next):
            last = last.next
 
            last.next = new_node

if __name__=='__main__':
 
    llist = LinkedList()
    llist.push(140)
    llist.append(141)
    llist.append(142)
    llist.append(143)
 
    print('Created linked list is: ')
    llist.printList()
 