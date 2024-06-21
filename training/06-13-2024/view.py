class node:
    def __init__(self,u):
        self.data=u
        self.left=None
        self.right=None
class tree:
    def __init__(self):
        self.root=None
    def create(self,root,x):
        if(root==None):
            return node(x)
        elif(root.data>x):
            root.left=self.create(root.left,x)
        else:
            root.right=self.create(root.right,x)
        return root
    def leftview(self,root,c,l):
        if(root is None):
            return
        if(c not in l):
            l.append(c)
            print(root.data)
        self.leftview(root.left,c+1,l)
        self.leftview(root.right,c+1,l)
    def rightview(self,root,c,l):
        if(root is None):
            return
        if(c not in l):
            l.append(c)
            print(root.data)
        self.rightview(root.right,c+1,l)
        self.rightview(root.left,c+1,l) 
    def topview(self,root):
        q=[(root,0)]
        tp=[]
        d={}
        while q: 
            n=len(q)
            while n:
                root,i=q.pop(0)
                if i not in d:
                    d[i]=root.data
                if root.left:
                    q.append((root.left,i-1))
                if root.right:
                    q.append((root.right,i+1))
                n-=1
        for i,j in sorted(d.items()):
            tp.append(j)
        print(tp)
    def bottomview(self,root):
        q=[(root,0)]
        bv=[]
        d={}
        while q:
            n=len(q)
            while n:
                root,i=q.pop(0)
                d[i]=root.data
                if root.left:
                    q.append((root.left,i-1))
                if root.right:
                    q.append((root.right,i+1))
                n-=1
        for i,j in sorted(d.items()):
            bv.append(j)
        print(bv)        
            
t1=tree()
t1.root=node(10)
t1.create(t1.root,5)
t1.create(t1.root,15)
t1.create(t1.root,2)
t1.create(t1.root,7)
t1.create(t1.root,11)
t1.create(t1.root,8)
t1.create(t1.root,9)
t1.leftview(t1.root,0,[])
t1.rightview(t1.root,0,[])
t1.topview(t1.root)
t1.bottomview(t1.root)
