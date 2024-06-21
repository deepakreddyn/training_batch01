d={5:[7,3],7:[5,3,4],3:[5,7,8],4:[2,7,8],8:[4,3,2],2:[4,8]}
l=[]
s=5
t=2
def fun(s,l):
    l.append(s)
    for i in d[s]:
        if(i not in l):
            fun(i,l)

fun(s,l)
print(l)
def all_paths(s, t, path=None):
    if path is None:
        path = []
    path.append(s)
    if s == t:
        print(" -> ".join(map(str, path)))
    else:
        for i in d[s]:
            if i not in path:
                all_paths(i, t, path.copy())
    path.pop()
all_paths(s,t)








