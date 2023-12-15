def mergeIntervals(intervals):

    intervals.sort(key=lambda i:i[0])
    res = [intervals[0]]
    for start,end in intervals[1:]:
        last=res[-1][1]

        if start<=last:
            res[-1][1]=max(last,end)
        else:
            res.append([start,end])
    return res


intervals=[[1,4],[0,3]]
print(mergeIntervals(intervals))


