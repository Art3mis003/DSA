class Interval:
    def __init__(self,s=0,e=0):
        self.start=s
        self.end=e

    def meetingRoom(self,intervals):
        intervals.sort(key=lambda i:i.start)
        for i in range(1,len(intervals)):
            i1=intervals[i-1]
            i2=intervals[i]
            if i1.end>i2.start:
                return False
        return True


intervals=[Interval(0,3),Interval(5,10),Interval(15,20)]
print(Interval().meetingRoom(intervals))

def meetingRoom(intervals):
    intervals.sort(key=lambda i:i[0])
    for i in range(1,len(intervals)):
        i1=intervals[i-1]
        i2=intervals[i]
        if i1[1]>i2[0]:
            return False
    return True

intervals=[[0,3],[5,10],[15,20]]
print(meetingRoom(intervals))