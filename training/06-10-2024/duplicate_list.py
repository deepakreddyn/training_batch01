a=[4,5,2,1,4,5,3]
#l2=[]
#l3=[]
#l4=[]
#l5=[]
#for i in l:
 #   if i not in l2:
  #      l2.append(i)
   # else:
    #    l3.append(i)
#for i in l3:
 #   if i not in l4:
  #      l4.append(i)
   # else:
    #    l5.append(i)
#print(l2,l4,l5)
m=[]
c=0
while(c!=len(a)):
    r=[]
    for i in range(len(a)):
        if(not str(a[i]).isalpha()):
            if(a[i] not in r):
                c=c+1
                r.append(a[i])
                a[i]='a'
    m.append(r)
print(m)

