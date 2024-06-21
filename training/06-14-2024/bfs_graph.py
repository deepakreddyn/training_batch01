d={5:[7,3],7:[5,3,4],3:[5,7,8],4:[2,7,8],8:[4,3,2,1],2:[4,8,9],9:[2,19],1:[8],19:[2]}
q=[5]
v=[]
while q:
    s = q.pop(0)
    if s not in v:
        v.append(s)
        for i in d[s]:
            if i not in v and i not in q:
                q.append(i)
print(v)          