def two_sum(array, target):
    l,r= 0, len(array)-1
    while l<r:
        sum= array[l]+array[r]
        if sum>target:
            r-=1
        elif sum<target:
            l+=1
        else:
            return [l+1, r+1]
    

