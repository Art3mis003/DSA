def kthElement(nums,k):
    k=len(nums)-k
    def quickselect(nums,l,r):
        pivot,p=nums[r],l
        for i in range(l,r):
            if nums[i]<=pivot:
                temp=nums[i]
                nums[i]=nums[p]
                nums[p]=temp
                p+=1
        nums[p],nums[r]=nums[r],nums[p]
        return p
    l,r= 0, len(nums)-1
    while l<r:
        pivot=quickselect(nums,l,r)

        if pivot>k:
            r-=1
        elif pivot<k:
            l+=1
        else:
            break
    return nums[k]

nums=[3,2,1,5,6,4]
k=1
print(kthElement(nums,k))



