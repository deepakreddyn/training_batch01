from collections import defaultdict
class TrieNode():
    def __init__(self):
        self.dict={}
        self.flag=False
        self.count=defaultdict(int)
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        node=self.root
        for i in word:
            if i not in node.dict:
                node.dict[i]=TrieNode()
            node.count[i]+=1
            node=node.dict[i]
        node.flag=True
n    def display(self):
        node=self.root
        res=[]
        def dfs(node,word):
            if node.flag==1:
                res.append(word[:])
            for i in node.dict.keys():
                dfs(node.dict[i],word+i)
        dfs(node,"")
        print(res)
    def search_word(self,word):
        node=self.root
        for i in word:
            if i not in node.dict:
                return False
            node=node.dict[i]
        if node.flag==1:
            return True
        return False
    def prefix(self,word):
        node=self.root
        flag=0
        res=float('inf')
        for i in word:
            res=min(res,node.count[i])
            if i not in node.dict.keys():
                break
            node=node.dict[i]
        return res
                
t1=Trie()
t1.insert("word")
t1.insert("apple")
t1.insert("words")
t1.insert("wo")
t1.display()
print(t1.search_word("words"))
print(t1.search_word("world"))
print(t1.prefix("wo"))