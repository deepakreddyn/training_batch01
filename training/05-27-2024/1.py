a=[1,5,8,9]
b=[2,7,9,10,14] 
c=[];i=0;j=0
for n in range(len(a)+len(b)):
    if not a:
        c.append(b[j])
        b.remove(b[0])
    elif not b:
        c.append(a[i])
        a.remove(a[0])
    elif a[0]>b[0]:
        c.append(b[j])
        b.remove(b[0])
    else:
        c.append(a[i])
        a.remove(a[0])
print(c)