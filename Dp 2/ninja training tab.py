def ninjaTraining(n,points):
    dp=[[-1 for i in range(4)] for j in range(n)]
    dp[0][3]=max(points[0][0],points[0][1],points[0][2])
    dp[0][0]=max(points[0][1],points[0][2])
    dp[0][1]=max(points[0][2],points[0][0])
    dp[0][2]=max(points[0][0],points[0][1])
    for day in range(1,n):
        for last in range(4):
            dp[day][last]=0
            for i in range(3):
                if i!=last:
                    activity=points[day][i]+dp[day-1][i]
                    dp[day][last]=max(dp[day][last],activity)
    return dp[n-1][3]

n=3
points=[[1,2,3],[4,5,6],[7,8,9]]
print(ninjaTraining(n,points))

