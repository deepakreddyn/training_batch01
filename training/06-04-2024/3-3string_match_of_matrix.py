mat=[]
n=int(input())
for i in range(n):
    out=[]
    for j in range(n):
        out.append(input())
    mat.append(out)
k=input()
flag=0
for i in range(len(k)):
    if k[i] not in mat[i%n]:
        print("No")
        flag=1
        break
if flag==0:
    print("Yes")
    
    
    
