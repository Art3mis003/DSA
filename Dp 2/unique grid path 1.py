def memoUnique(m,n):
    dp=[[-1 for i in range(n+1)] for j in range(m+1)]
    def helper(m,n):
        if m==0 and n==0:
            return 1
        if m<0 or n<0:
            return 0
        if dp[n][m]!=-1:
            return dp[n][m]
        up= helper(n-1,m)
        left=helper(n,m-1)
        dp[n][m]=up+left
        return dp[n][m]
    return helper(n-1,m-1)

m=3
n=2
print(memoUnique(m,n))





