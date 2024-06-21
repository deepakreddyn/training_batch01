a=[1,2,3,4,5]
b=[1,2,3,4,5]
i=0;j=0
esum=0;osum=0
def solve(a,b,i,j,esum,osum):
    if i>=len(a) & j>=len(b):
        return esum,osum
    if a[i]%2==0:
        esum+=a[i]
    if b[j]%2!=0:
        osum+=b[j]
    return solve(a,b,i+1,j+1,esum,osum)
print(solve(a,b,i,j,esum,osum))
