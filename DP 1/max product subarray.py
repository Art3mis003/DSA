def prodSub(nums):
    if not nums:
        return 0
    res = max(nums)
    n = len(nums)
    dp_max = [1] * n
    dp_min = [1] * n
    dp_max[0] = nums[0]
    dp_min[0] = nums[0]
    for i in range(1, len(nums)):
        if nums[i] == 0:
            dp_min[i], dp_max[i] = 1, 1
            continue
        dp_min[i] = min(nums[i], nums[i] * dp_min[i - 1], nums[i] * dp_max[i - 1])
        dp_max[i]=max(nums[i],nums[i]*dp_min[i-1], nums[i] * dp_max[i - 1])
        res=max(res,dp_max[i])
    return res

nums=[3,-1,4]
print(prodSub(nums))
