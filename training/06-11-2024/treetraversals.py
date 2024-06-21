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
    def inorder(self,root):
        if(root):
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)
    def preorder(self,root):
        if(root):
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)
        return
    def postorder(self,root):
        if(root):
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)
    def sumorder(self,root):
        if(root is None):
            return 0
        return root.data +self.sumorder(root.left)+self.sumorder(root.right)
    def even(self,root):
        if(root==None):
            return 0
        if(root.data%2==0):
            return root.data+self.even(root.left)+self.even(root.right)
        return self.even(root.right)+self.even(root.left)
    def odd(self,root):
        if(root==None):
            return 0
        if(root.data%2!=0):
            return root.data+self.odd(root.left)+self.odd(root.right)
        return self.odd(root.right)+self.odd(root.left)
    
    def diff(self,root):
        if(root==None):
            return 0
        if(root.data%2==0):
            return root.data+self.diff(root.left)+self.diff(root.right)
        return self.diff(root.right)+self.diff(root.left)-root.data
    def height(self,root):
        if(root==None):
            return -1
        return max(self.height(root.left),self.height(root.right))+1
    def balance(self,root):
        return abs(self.height(root.left)-self.height(root.right))<=1
    def leafnodes(self,root):
        if(root is None):
            return 0
        if(root.left==None and root.right==None):
            return 1   
        return self.leafnodes(root.left)+self.leafnodes(root.right)
    def sumleaf(self,root):
        if(root is None):
            return 0
        if(root.left==None and root.right==None):
            return root.data   
        return self.sumleaf(root.left)+self.sumleaf(root.right)
    def search(self,root,x):
        if(root is None):
            return'not found'
        elif(x==root.data):
            return 'found'
        elif(x>root.data):
            return self.search(root.right,x)
        else:
            return self.search(root.left,x)
    def depth(self,root,x,c):
        if(root is None):
            return'not found'
        elif(x==root.data):
            return c
        elif(x>root.data):
            return self.depth(root.right,x,c+1)
        else:
            return self.depth(root.left,x,c+1)
t1=tree()
t1.root=node(10)
t1.create(t1.root,5)
t1.create(t1.root,15)
t1.create(t1.root,25)
t1.create(t1.root,35)
print(t1.sumorder(t1.root))
print(abs(t1.diff(t1.root)))
print(t1.even(t1.root))
print(t1.odd(t1.root))
print(t1.height(t1.root))
t1.balance(t1.root)
if(t1.balance(t1.root)):
    print("balance")
else:
    print("not balance")
print(t1.leafnodes(t1.root))
print(t1.sumleaf(t1.root))
print(t1.search(t1.root,5))
print(t1.depth(t1.root,35,0))