import heapq
def handsofStraight(group,hand):
    if len(hand)% group:
        return False
    count={}
    for n in hand:
        count[n]= 1+ count.get(n,0)
    minHeap= list(count.keys())
    heapq.heapify(minHeap)

    while minHeap:
        first= minHeap[0]
        for i in range(first,first+group):
            if i not in count:
                return False
            count[i]-=1
            if count[i]==0:
                if i!=minHeap[0]:
                    return False
                heapq.heappop(minHeap)
    return True


hands=[1,2,3,6,2,3,4,6,8]
group=3
print(handsofStraight(group,hands))



