from http.client import NETWORK_AUTHENTICATION_REQUIRED


class Node:
    def __init__(self,value):
        self.value=value
        self.next= None

class linklist:
    def __init__(self):
        self.point= None

    def insert (self, node):
        new_node=Node(node)
        new_node.next= self.point
        self.point=new_node

    def addtoend(self, data):
        new_node=Node(data)

        if self.point is None:
            self.point= new_node
            return
        last=self.point
        while(last.next):
            last=last.next
        last.next=new_node
    
    def printlist(self):
        x=self.point
        while (x):
            print(x.value, end=">>")
            x=x.next 

if __name__=='__main__':
    list=linklist()
    list .addtoend(10) 
    list.addtoend(20)   
    list.addtoend(15)
    list.printlist()


