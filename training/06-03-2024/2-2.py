def fu(x):
    if(x==0):
        return 0
    return x+fu(x-2)
n=int(input())
if(n%2==0):
    print(fu(n))
else:
    print(fu(n-1))