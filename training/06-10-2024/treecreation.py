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
    def evenoddsum(self,root):
        es=0
        os=0
        if(root is None):
            return 0
        if(root.data%2==0):
            es=root.data+es
        else:
            os=root.data+os
        self.evenoddsum(root.left)
        self.evenoddsum(root.right)
        print(es)
        print(os)
        
t1=tree()
t1.root=node(10)
t1.create(t1.root,5)
t1.create(t1.root,15)
t1.create(t1.root,25)
t1.create(t1.root,35)
print(t1.sumorder(t1.root))
t1.evenoddsum(t1.root)
