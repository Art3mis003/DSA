import heapq
from collections import Counter
import collections
def Task(tasks,n):
    count=  Counter(tasks)
    maxHeap=[-c for c in count.values()]
    q= collections.deque()
    time=0
    heapq.heapify(maxHeap)
    while maxHeap or q:
        time += 1
        if maxHeap:
            t = 1+heapq.heappop(maxHeap)
            if t:
                q.append([t,time+n])

        if q and q[0][1]==time:
            heapq.heappush(maxHeap, q.popleft()[0])
    return time

tasks=["A","A","A","B","B","B"]
n=1 
print(Task(tasks,n))



