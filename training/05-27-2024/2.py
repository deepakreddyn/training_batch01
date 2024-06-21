s="aaabbaaaaddd"
s1="a";s2=""
l=[]

for i in range(len(s)):
    if s[i]==s1:
        l.append(s1)
    else:
        s2+=s1
        s2+=str(len(l))
        l.clear()
        s1=s[i]
        l.append(s1)
s2+=s1
s2+=str(len(l))
print(s2)