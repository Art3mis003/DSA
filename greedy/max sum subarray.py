def MaxSub(nums):
    maxSub=nums[0]
    curSum=0
    for n in nums:
        curSum+=n
        maxSub = max(maxSub, curSum)
        if curSum<0:
            curSum=0

    return maxSub 

nums=[-1,-9,-5,-5,-3,-2]
print(MaxSub(nums))
