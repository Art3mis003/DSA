def minOver(intervals):
    intervals.sort(key=lambda i:i[0])
    count=0
    prev= intervals[0][1]
    for start,end in intervals[1:]:
        if start<prev:
            count+=1
            prev=min(end,prev)
        else:
            prev=end
    return count

intervals=[[1,2],[2,3],[3,4],[1,3]]
print(minOver(intervals))







