a=list(map(int,input().split()))
for i in range(len(a)-2):
    s=a[i]+a[i+1]+a[i+2]
    a[i]=min(a[i],a[i+1],a[i+2])
    a[i+2]=max(a[i],a[i+1],a[i+2])
    a[i+1]=s-a[i+2]-a[i]
print(a)
        
        