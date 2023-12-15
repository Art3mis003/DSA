def subset(nums):
    res=[]
    subset = []

    def dfs(i):
        if i >= len(nums):
            print(subset)
            res.append(subset.copy())
            return
        # decision to include nums[i]
        subset.append(nums[i])
        # print('here1 '+str(i))
        dfs(i + 1)
        # decision NOT to include nums[i]
        subset.pop()
        # print('here2 ' + str(i))
        dfs(i + 1)

    dfs(0)
    return res



nums=[1,2,3]
result=subset(nums)
print(result)