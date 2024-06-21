n=int(input())
s=set()
d=[]
c=0
for i in range(n):
    k=int(input())
    str1=input()
    if k==1:
        s.add(str1)
    elif k==2:
        if str1 in s:
            d.append("True")
        else:
            d.append("False")
    elif k==3:
        for i in s:
            if i[0:len(str1)]==str1:
                c=c+1
        d.append(c)
    else:
        if str1 in s:
            s.remove(str1)
print(s)
for i in d:
    print(i)