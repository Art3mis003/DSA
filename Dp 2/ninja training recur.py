def ninjaTraining(n, points):
    """memoization is mix of recursion and dp"""

    def f(day, last):
        maxi = 0
        if (day == 0):

            for i in range(3):
                if (i != last):
                    maxi = max(maxi, points[0][i])
        return maxi

        maxi = 0
        for i in range(3):
            if (i != last):
                activity = points[day][i] + f(day - 1, i)
                maxi = max(activity, maxi)
        return maxi

    return f(n - 1, 3)

n=3
points=[[1,2,3],[4,5,6],[7,8,9]]
print(ninjaTraining(n,points))





