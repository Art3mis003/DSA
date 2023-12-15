def maxSubArray(array,k):
    maxSum= float('-inf')
    windowSum= sum(array[:k])
    for i in range(k,len(array)):
        windowSum+= array[i] - array[i-k]
        maxSum= max(windowSum, maxSum)
    return maxSum

array=[1,2,3,4,5,6,7,8,9,10]
k=2
print(maxSubArray(array,k))