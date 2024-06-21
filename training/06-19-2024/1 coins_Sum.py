s=[2,3,5,6]
n=7
mp={}
def sub_set(idx,out):
    if out==n:
        return 1
    if idx==len(s):
        return 0
    if (idx,out) in mp:
        return mp[(idx,out)]
    take=sub_set(idx+1,out+s[idx])
    not_take=sub_set(idx+1,out)
    mp[(idx,out)]=(take or not_take)
    return mp[(idx,out)]
def solve():
    dp=[[0 for i in range(n+1)]for j in range(len(s))]
    for i in range(n+1):
        if i==0 or i==s[0]:
            dp[0][i]=1
    for i in range(1,len(s)):
        for j in range(n+1):
            if j<s[i]:
                dp[i][j]=dp[i-1][j]
            else:
                if dp[i-1][j-s[i]]==0:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j-s[i]]
    print(dp)
    if dp[-1][-1]:
        print("Yes")
    else:
        print("No")
            
solve()