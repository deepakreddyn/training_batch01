l=list(map(int,input().split()))
k=int(input())
def combination(l,k):
    def fun(c,s):
        if(len(c)==k):
            print(c)
            return
        for i in range(s,len(l)):
            fun(c+[l[i]],i+1)
        return
    fun([],0)
combination(l,k)
    
#for i in range(len(l)-2):
#    for j in range(i+1, len(l)):
#       for k in range(j+1, len(l)):
#            print(l[i], l[j], l[k])


