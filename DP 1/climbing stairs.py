def climbing(n):
    """ways to climb n stairs; add all choices"""
    dp=[-1]*(n+1)
    dp[0]=1
    dp[1]=1


    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-1]
    return dp[n]

n=1
print(climbing(n))