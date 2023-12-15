def  productExceptSelf( nums) :
    answer = [1] * (len(nums))
    prefix=1
    for i in range(len(nums)):
        answer[i]=prefix
        prefix = nums[i]*prefix
    postfix=1
    for i in range(len(nums)-1,-1,-1):
        answer[i]= answer[i]*postfix
        postfix = postfix * nums[i]
    return answer

array=[1,2,3,4]
print(productExceptSelf(array))
