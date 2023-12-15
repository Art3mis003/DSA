def maxProd(nums):
    n=len(nums)
    prefix,suffix=nums[0],nums[n-1]
    res=max(nums[0],nums[n-1])

    for i in range(1,n):
        if nums[i]==0:
            prefix=1
            suffix=1
        prefix=prefix*nums[i]
        suffix=suffix*nums[n-1-i]
        res=max(prefix,suffix,res)
    return res

nums=[3,-1,4]
print(maxProd(nums))
