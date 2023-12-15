import heapq
def Kthelement(nums,k):
    minHeap = []
    for i in range(k):
        minHeap.append(nums[i])
        heapq.heapify(minHeap)
    for i in range(k, len(nums)):
        if nums[i] > minHeap[0]:
            heapq.heappop(minHeap)
            heapq.heappush(minHeap, nums[i])
    return minHeap[0]