a=[1,1,1,1,5,8]
c=1
b=a[0]
def frequent(a):
    for i in range(1,len(a)):
        if(a[i]==b):
            c=c+1
        else:
            c=c-1
            if(c==0):
                c=1
                b=a[i]
print(b)