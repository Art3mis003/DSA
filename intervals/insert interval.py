def insert(new,intervals):
    res=[]
    for i in range(len(intervals)):
        #if new interval comes before the current
        if new[1]<intervals[i][0]:
            res.append(new)
            return res + intervals[i:] #since new interval is added and hence no more overlapping.
        # if new interval comes after the current
        elif new[0]>intervals[i][1]:
            res.append(intervals[i]) #since current is added new is not added cause might overlap with next
        else:
            new= [min(new[0],intervals[i][0]), max(new[1],intervals[i][1])] #decide new intervals overalpping with current
    res.append(new)
    return res

new=[2,5]
intervals=[[1,3],[6,9]]
print(insert(new,intervals))
