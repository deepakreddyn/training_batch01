n=int(input())
k=0
for i in range(n):
    for j in range(n):
        if(i==0 or j==0 or i==n-1 or j==n-1):
            print("1",end=' ')
        if(i==1 or j==1 or i==n-1 or j==n-1):
            print("2",end=' ')
        else:
            print(k,end=' ')
            k=k+1
    print()