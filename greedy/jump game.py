def jumpGame(nums):
    p= len(nums)-1
    for i in range(len(nums)-1,-1,-1):
        if i+nums[i]>=p:
            p=i
    if p==0:
        return True
    else:
        return False


nums=[2,2,1,0,4]
print(jumpGame(nums))

