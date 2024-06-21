mat=[]
n=int(input())
for i in range(n):
    mat.append(list(input()))
k=input()
flag=0
for i in range(len(k)):
    if k[i] not in mat[i%n]:
        print("No")
        flag=1
        break
    else:
        m[i].remove(s[i])
if flag==0:
    print("Yes")
    
    
    

