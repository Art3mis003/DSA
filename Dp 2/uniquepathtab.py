def uniquePathTab(m,n,obs):
    dp=[[-1 for i in range(n)]for j in range(m)]
    
    for i in range(m):
        for j in range(n):
            if i==0 and j==0:
                dp[i][j]=1
                continue
            if i>0 and j>0 and obs[i][j]==1:
                dp[i][j]=0
                continue
            up,left=0,0
            if i>0:
                up=dp[i-1][j]
            if j>0:
                left=dp[i][j-1]
            dp[i][j]=up+left

    return dp[m-1][n-1]

obs=[[0,1],[0,0]]
m=len(obs)
n=len(obs[0])
print(uniquePathTab(m,n,obs))



