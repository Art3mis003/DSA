def combinationSum2(nums,target):
    res=[]
    ds=[]


    def dfs(i,target):
        if target==0:
            return res.append(ds[:])
        if i>=len(nums) or target<0:
            return

        for k in range(i,len(nums)):
            if k>i and nums[k]==nums[k-1]:
                continue
            if nums[k]>target:
                break
            ds.append(nums[k])
            dfs(k+1,target-nums[k])
            ds.pop()



    nums.sort()
    dfs(0,target)
    return res


nums=[1,1,1,2,2]
target=4
print(combinationSum2(nums,target))