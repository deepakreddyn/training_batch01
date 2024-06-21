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
    def oediff(self,t,os,es):
        if(t==None):
            return abs(es-os)
        if(t.data%2==0):
            es=es+t.data
        else:
            os=os+t.data
        return self.oediff(t.nxt,os,es)
l1=dll()
l1.head=node(10)
l1.tail=l1.head
l1.addback(20)
l1.addback(30)
l1.addback(40)
l1.addfront(50)
l1.addback(60)
l1.display()
print()
print(l1.oediff(l1.head,0,0))
