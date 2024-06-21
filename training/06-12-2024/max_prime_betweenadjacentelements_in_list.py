a=list(map(int,input().split()))
s=0
for i in range(len(a)-1):
    for k in range(a[i+1],a[i],-1):
        for j in range(2,(k//2)+1):
            if (k % j) == 0:
                break
        else:
            s=s+k
            break    
print(s)