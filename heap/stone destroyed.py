import heapq
class sol:
    def Stone(self,stones):

        #python does not have a max heap
        #hence use minheap and multiply by -1
        stones=[-s for s in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            first= heapq.heappop(stones)
            second=heapq.heappop(stones)
            if abs(second)<abs(first):
                heapq.heappush(stones, first - second)
        print(stones)
        stones.append(0)
        print(stones)
        return abs(stones[0])

stones=[8,14,24]
print(sol().Stone(stones))