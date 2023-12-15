def minIntervals(inters, queries):
    res=[]

    inters.sort(key=lambda i:i[0]) #don't sort queries
    for q in queries:
        num = float('inf')
        for start, end in inters[0:]:
            if q>=start and q<=end:
                num=min(num, end-start+1)
        if num==float('inf'):
            res.append(-1)
        else:
            res.append(num)
    return res

inters=[[2,3],[2,5],[1,8],[20,25]]
queries=[2,19,5,22]
print(minIntervals(inters, queries))



