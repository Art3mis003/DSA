def Combination(nums,t):
    res=[]
    def dfs(i,total,curr):
        if total==t:
            res.append(curr[:])
            return
        if i>=len(nums) or total>t:
            return

        curr.append(nums[i])
        dfs(i,total+nums[i],curr)
        curr.pop()
        dfs(i + 1, total, curr)

    dfs(0,0,[])
    return res

nums=[1,2,3,4,5]
t=0
print(Combination(nums,t))