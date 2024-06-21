l=[6,3,2,9,4,7]
l1=[8,7,5,3,6,9]
res=[]
s=0
l3=[]
def add(l,l1,i,j):
    global s
    if(i==len(l)):
        return 
    if (j==len(l1)):
        add(l,l1,i+1,0)
        s=0
        return 
    if l[i]%2==0:
        if l1[j]%2!=0:
            s=s+(l[i]+l1[j])
            res.append((l[i]+l1[j]))
        add(l,l1,i,j+1)
    else:
        l3.append(s)
        s=0
        add(l,l1,i+1,j)
add(l,l1,0,0)
print(res)
print(l3)