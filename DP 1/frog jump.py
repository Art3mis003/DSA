

def frogJump(n, heights) :
    dp = [0] * n
    dp[0] = 0
    s, ss = 0, float('inf')
    for i in range(1, n):
        if i > 1:
            ss = abs(heights[i] - heights[i-2]) + dp[i - 2]
        s = abs(heights[i] - heights[i-1]) + dp[i - 1]

        dp[i] = min(s, ss)
    return dp[n - 1]

heights= [10, 20, 30, 10]
n=len(heights)
print(frogJump(n,heights))
