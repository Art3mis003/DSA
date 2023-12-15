def Circlehouse(nums):
    def house(nums):
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        if n > 1:
            dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        return max(dp[n - 1], dp[n - 2])
    return max(house(nums[:-1]), house(nums[1:]))

house=[2,3,2]
print(Circlehouse(house))