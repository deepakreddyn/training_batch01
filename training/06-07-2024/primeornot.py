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
    def primecount(self,t,c):
        if(t==None):
            return c
        def is_prime(s,n):
            if(s>=(n//2)+1):
                return 1
            if(n%s==0):
                return 0
            return is_prime(s+1,n)
        if(is_prime(2,t.data)):
            c=c+1
        return self.primecount(t.nxt,c)
l1=dll()
l1.head=node(10)
l1.tail=l1.head
l1.addback(2)
l1.addback(3)
l1.addback(40)
l1.addfront(5)
l1.addback(60)
l1.display()
print()
print(l1.primecount(l1.head,0))

