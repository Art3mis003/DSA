def subset2(nums):
    ans=[]
    ds=[]
    def dfs(ind):
        ans.append(ds[:])
        print(ans)
        for i in range(ind,len(nums)):
            if i!=ind and nums[i]==nums[i-1]:
                continue

            ds.append(nums[i])
            print(ds)
            dfs(i+1)
            print(ds)
            ds.pop()
            print(ds)
    nums.sort()
    dfs(0)
    return ans
nums=[1,2,2,3]
subset2(nums)