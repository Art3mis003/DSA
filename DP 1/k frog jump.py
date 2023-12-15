def frogK(n,k,nums):
    dp = [0] * n
    dp[0] = 0

    for i in range(1, n):
        s = float('inf')
        for j in range(1, k + 1):
            if i - j >= 0:
                jump= dp[i - j] + abs(nums[i] - nums[i - j])
                s= min(s, jump)
        dp[i]+= s
    return dp[n - 1]

nums=[10,40,30,10]
n=len(nums)
k=2
print(frogK(n,k,nums))