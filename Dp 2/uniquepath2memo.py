def uniquePathMem(m,n,obs):
    dp=[[-1 for i in range(n) ]for j in range(m)]
    def helper(i,j):
        if i==0 or j==0:
            return 1
        if i<0 or j<0 or obs[i][j]==1:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        up=helper(i-1,j)
        left=helper(i,j-1)
        dp[i][j]=up+left
        return dp[i][j]
    return helper(m-1,n-1)



obs=[[0,0,0],[0,1,0],[0,0,0]]
m=len(obs)
n=len(obs[0])

print(uniquePathMem(m,n,obs))
