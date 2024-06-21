n=[]
n=list(map(int,(input().split(" "))))
def fun(n):
    if(len(n)==0):
        return 0
    if(len(n)==1):
        return n[0]
    if (len(n)==2):
        return max(n)
    le=n[0]+fun(n[2:])
    ri=n[0]+fun(n[3:])
    return max(le,ri)
print(fun(n))
    