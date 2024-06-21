a=input()
s='abcdefghijklmnopqrstuvwxyz'
c=0  
for i in s:
    if i not in a:
        c=1
        break
if(c==1):
    print("no")
else:
    print("yes")