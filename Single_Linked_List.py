#Operation on Adding a Node Begining Ending
class Node:
    def __init__(self):
        self.data = data 
        self.ref = None
    
class Linklist:
    def __init__(self):
        self.head = None


    def LL_Print(self):
        if self.head in  None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,"----------->",end=" ")
                n= n.ref
            
    def Add_begin(self,data):
        New_node = Node(data)
        New_node.ref = self.head
        self.head = New_node


    def Add_end(self,data):
        New_node = Node(data)#creating the new node help of Node(data) class
        if self.head is None:   #check head is null or not
            self.head = New_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            
            n.ref = New_node

ll1 = Linklist()
ll1.Add_begin(10)
ll1.Add_end(30)
ll1.Add_begin(50)
ll1.LL_Print()
