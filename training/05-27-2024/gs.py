def getSum(n): 
    sum1 = 0
    for digit in str(n):
        sum1 += int(digit)
    if sum1<=9:
        return sum1
    return getSum(sum1)
        
n = int(input())
while True:
    res=getSum(n)
    if res in [2,3,5,7]:
        print(n)
        break
    n=n+1
    

    