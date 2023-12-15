import heapq

class sol:
    def __init__(self, k, nums):
        self.minHeap,self.k= nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
    def add(self, val):
        heapq.heappush(self.minHeap,val)
        if len(self.minHeap)>k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


nums=[4,5,8,0]
k=4
print(sol(k,nums).add(1))