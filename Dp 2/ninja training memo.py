
def f(day, last, points, dp):
    # Check if the result for this day and last activity is already computed.
    if dp[day][last] != -1:
        return dp[day][last]

    # Base case: When we reach day 0, return the maximum point for the last day.
    if day == 0:
        maxi = 0
        for i in range(3):
            if i != last:
                maxi = max(maxi, points[0][i])
        dp[day][last] = maxi
        return dp[day][last]

    maxi = 0
    # Iterate through all activities for the current day.
    for i in range(3):
        if i != last:
            # Calculate the total points for the current day's activity and recursively call for the previous day.
            activity = points[day][i] + f(day - 1, i, points, dp)
            maxi = max(maxi, activity)

    # Store the maximum points in the DP table and return it.
    dp[day][last] = maxi
    return dp[day][last]

def ninjaTraining(n, points):
    # Initialize a DP table to store the computed results.
    dp = [[-1 for j in range(4)] for i in range(n)]
    # Start the recursive function from the last day with no previous activity.
    return f(n - 1, 3, points, dp)



points=[[1,2,3],[4,5,6],[7,8,9]]
n = len(points)

print(ninjaTraining(n, points))

