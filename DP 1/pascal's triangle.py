def Pascal1(numR):
    dp=[0]*numR
    for i in range(numR):
        dp[i]=[1]*(i+1)
        for j in range(1,i):
            dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
    return dp

number=5
print(Pascal1(number))
