n=list(map(int,input().split(" ")))
buy=n[0]
p=0
for i in range(1,len(n)):
    if n[i]<buy:
        buy=n[i]
    else:
        p=max(p,n[i]-buy)
print(p)
