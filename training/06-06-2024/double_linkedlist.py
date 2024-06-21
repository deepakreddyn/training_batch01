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
    def rev_display(self):
        t=self.tail
        while(t!=None):
            print(t.data, end="<->")
            t=t.prev
    def search(self,x):
        t=self.head
        t1=self.tail
        while(t!=t1 and t!=t1.nxt):
            if(t.data==x or t1.data==x):
                return 1
            t=t.nxt
            t1=t1.prev
        if(t.data==x):
            return 1
        else:
            return 0
    def length(self):
        t=self.head
        t1=self.tail
        while(t!=t1 and t!=t1.nxt):
            t=t.nxt
            t1=t1.prev
        if(t==t1):
            return "odd"
        else:
            return "even"
    def checkpalin(self):
        t=self.head
        t1=self.tail
        while(t!=t1 and t!=t1.nxt):
            if(t.data!=t1.data):
                return "npalindrome"
            t=t.nxt
            t1=t1.prev
        return "palindrome"
    def half(self):
        if self.head is None:
            print("List is empty")
            return
        slow = self.head
        fast = self.head
        while (fast!=None and fast.nxt!=None):
            slow = slow.nxt
            fast = fast.nxt.nxt
        t1=slow
        t=self.head
        while(t1!=None):
            t.data,t1.data=t1.data,t.data
            t=t.nxt
            t1=t1.nxt   
l1=dll()
l1.head=node(4)
l1.tail=l1.head
l1.addback(50)
l1.addback(30)
l1.addback(20)
l1.addfront(87)
l1.addback(10)
l1.addback(40)
l1.addback(67)
l1.display()
print()
print()
print(l1.search(40))
print(l1.length())
print(l1.checkpalin())
l1.half()
l1.display()


   