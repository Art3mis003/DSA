def water_container(heights):
    l,r= 0, len(heights)-1
    result=0
    while l<r:
        area= (r-l)* min(heights[l], heights[r])
        result= max(result, area)
        if heights[l]<heights[r]:
            l+=1
        elif heights[r]<heights[l]:
            r-=1
        else:
            if heights[l+1]>heights[r-1]:
                l+=1
            else:
                r-=1
    return result

arra=[1,8,6,2,5,4,8,3,7]
print(water_container(arra))