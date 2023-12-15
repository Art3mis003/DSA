def CostClimb(cost):
    n=len(cost)
    for i in range(2,n):
        cost[i]+=min(cost[i-1],cost[i-2])
        print(cost)
    return min(cost[n-1],cost[n-2])

cost=[1,100,1,1,1,100,1,1,100,1]
print(CostClimb(cost))


