d={5:[(7,2),(3,1)],7:[(5,2),(3,2),(4,1)],3:[(5,1),(7,2),(8,2)],4:[(2,1),(7,1),(8,1)],8:[(4,1),(3,2),(2,1)],2:[(4,1),(8,1)]}
l=[]
s=5
def cost_path(s,t,c,m,l1):
    l.append(s)
    if s == t:
        if(c<m):
            m=c
            l1=l.copy()
        l.pop()
        return m,l1
    else:
        for i, w in d.get(s, []):
            if i not in l:
               m,l1=cost_path(i, t, c + w,m,l1)
    
    l.pop()
    return m,l1
for i in d.keys():
    print(cost_path(s,i,0,99999,[]))

