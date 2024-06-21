def island(i,j):
    if(i<0 or j<0)
    
    
    
    
    
    
    return c
m=0
n=5
co=0
a=[][]
for  i in range(n):
    for j in range(n):
        if(a[i][j]==1):
            k=fun(i,j,0)
            if(k>m):
                m=k
            co=co+1
print(co,m)








ip=[[0,1,0,0,1],[1,0,0,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,0,0,0,1]]
res=-float('inf')
def dfs(ip,i,j):
    if i>=len(ip) or j>=len(ip) or i<0 or j<0 or ip[i][j]==0:
        return 0
    ip[i][j]=0
    out=1
    out+=dfs(ip,i+1,j)
    out+=dfs(ip,i,j+1)
    out+=dfs(ip,i-1,j)
    out+=dfs(ip,i,j-1)
    return out
for i in range(len(ip)):
    for j in range(len(ip)):
        if ip[i][j]==1:
            res=max(res,dfs(ip,i,j))
print(res)