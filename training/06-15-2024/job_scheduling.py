n=[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
a=[5,6,5,4,11,2]
l=a.copy()
s=0
for i in range(1,len(n)):
    for j in range(0,i):
        if n[j][1]<=n[i][0]:
            l[i]=max(l[i],l[j]+a[i])
print(l)
print(max(l))
