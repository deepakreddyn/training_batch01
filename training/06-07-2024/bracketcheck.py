class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def addback(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            t=node(x)
            self.tail.nxt=t
            t.prev=self.tail
            self.tail=self.tail.nxt
    def addfront(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            t=node(x)
            t.nxt=self.head
            self.head.prev=t
            self.head=t
            
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data, end="<->")
            t=t.nxt
    def string(self):
        t=self.head
        c=0
        while(t!=None):
            print(t.data, end="<->")
            t=t.nxt
l1=dll()
l1.head=node('[')
l1.tail=l1.head
l1.addback('(')
l1.addback(')')
l1.addback(']')
l1.addfront('{')
l1.addback('}')
l1.display()