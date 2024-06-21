class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
class sll:
    def __init__(self):
        self.head=None
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data, end="->")
            t=t.nxt
    def addback(self,x):
        t=self.head
        while(t.nxt!=None):
            t=t.nxt
        t.nxt=node(x)
    def addfront(self,x):
        t= node(x)
        t.nxt = self.head
        self.head = t
        
    def addeven(self):
        t=self.head
        s=0
        while(t!=None):
            if(t.data%2==0):
                s=s+t.data
            t=t.nxt
        print()
        print(s)
    def sea(self,x):
        t=self.head
        while(t!=None):
            if(t.data==x):
               return "found"
            t=t.nxt
        return"notfound"
    def midele(self):
        if self.head is None:
            print("List is empty")
            return
        slow = self.head
        fast = self.head
        while (fast!=None and fast.nxt!=None):
            slow = slow.nxt
            fast = fast.nxt.nxt
        return slow.data
    def middle(self):
        if self.head is None:
            print("List is empty")
            return True 
        fast = self.head
        while fast and fast.nxt:
            fast = fast.nxt.nxt

        if fast is None:
            print("even")
            return True
        else:
            print("odd")
            return False
    def highestseq(self):
        c=1
        m=0
        t=self.head
        while(t.nxt!=None):
            if ((t.data)+1==t.nxt.data):
                c=c+1
            else:
                if(c>m):
                  m=c
                c=1
            t=t.nxt
        if(c>m):
            m=c
        print(m)
    def pair(self):
        t=self.head
        while(t!=None):
            t1=t.nxt
            while(t1!=None):
                print(t.data,t1.data)
                t1=t1.nxt
            t=t.nxt
    def bubblesort(self):
        t=self.head
        p=None
        while(t.nxt!=None):
            f=0
            t1=self.head
            while(t1.nxt!=p):
                if(t1.data>t1.nxt.data):
                    f=1
                    t1.data, t1.nxt.data =t1.nxt.data, t1.data
                t1=t1.nxt
            if(f==0):
                break
            p=t1
            t=t.nxt

l1=sll()
l1.head=node(1)
l1.addback(12)
l1.addback(3)
l1.addback(4)
l1.addback(50)
l1.addfront(100)
l1.display()
l1.bubblesort()
l1.display()


