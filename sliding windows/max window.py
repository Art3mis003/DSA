import collections


def maxWindow(nums,k):
    l=r=0
    op=[]
    queue= collections.deque()
    while r<len(nums):
        while queue and nums[queue[-1]]<nums[r]:
            queue.pop()
        queue.append(r)
        if l>queue[0]:
            queue.pop()

        if (r+1)>=k:
            op.append(nums[queue[0]])
            l+=1
        r+=1
    return op
nums=[1,3,-1,-3,5,3,6,7]
k=3
print(maxWindow(nums,k))

