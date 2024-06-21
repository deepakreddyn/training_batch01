    c=0
    def fun(i,j):
        if(i<0 or j<0 or i>=n or j>=n or a[i][j]!=1):
            return
        if(a[i][j]==1):
            a[i][j]=2
        fun(a[i-1][j])#up
        fun(a[i][j-1])#left
        fun(a[i+1][j])#down
        fun(a[i][j+1])#right
        return
fun(i,j)
for i in range(n):
    for j in range(n):
        if(a[i][j]==1):
            c=c+1