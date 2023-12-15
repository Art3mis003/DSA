def HouseRob(nums):
    n=len(nums)
    dp=[0]*n
    dp[0]=nums[0]
    dp[1]=max(nums[0],nums[1])

    for i in range(2,n):
        dp[i]=max(nums[i-1],nums[i-2]+nums[i])
        print(dp)
    return max(dp[n-2],dp[n-1])

house=[2,7,9,3,1]
print(HouseRob(house))


