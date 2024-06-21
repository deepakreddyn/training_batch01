password=input()
up,lc,d,s=0,0,0,0
for i in password:
    if i.isdigit():
        d+=1
    elif i.isupper():
        up+=1
    elif i.islower():
        lc+=1
    else:
        s+=1
res=0
if d==0:
    res+=1
if up==0:
    res+=1
if lc==0:
    res+=1
if s==0:
    res+=1
if res==0:
    print(-1)
elif len(password)<8:
    if (len(password)+res)>=8:
        print(res)
    else:
        print(8-len(password))
else:
    print(res)   

