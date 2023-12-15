def longestConsecutive(nums):
    numSet= set(nums)

    longest=0;
    for n in nums:
        if(n-1) not in numSet:
            length = 0;
            while(n+length)in numSet:
                length+=1
            longest= max(length, longest)
    return longest



array= [5,6,7,4,3,0,10]
n= longestConsecutive(array)

print(n)
