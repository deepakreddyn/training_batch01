import math
n=int(input())
k=int(input())
e=math.gcd(n,k)
if (e!=1):
    print("not co primes")
else:
    print("co primes")



# a=3 b=2 for i in range(2,(min(a,b)//2+1): if(a%i==0) and (b%i==0):  print("ncp")  break  else:print("cp")