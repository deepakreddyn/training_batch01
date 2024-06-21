#ip: 12321
n=int(input())
def fun(x,re):
    if(x==0):
        return re
    re=re*10+(x%10)
    return fun(x//10,re)
if 
