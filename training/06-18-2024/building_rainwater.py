n=[9,4,5,6,2,4]
s=0
l=[0]*len(n)
l1=[0]*len(n)
m=0
for i in range(len(n)):
    if(n[i]>m):
         m=n[i]
    l[i]=m
m1=0
for i in range(len(n)-1,-1,-1):
    if(n[i]>m1):
        m1=n[i]
    l1[i]=m1
print(l,l1)
for i in range(len(n)):
    s=s+min(l[i],l1[i])-n[i]
print(s) 