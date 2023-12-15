
def partitionLabels(s):
    last={}
    res=[]
    ind,l=0,len(s)
    for i in range(l):
        c= s[i]
        last[c]=i

    size,end=0,0

    while ind<l:
        c=s[ind]
        end= max(end,last[c])
        size += 1

        if end==ind:
            res.append(size)
            size=0
        ind+=1
    return res

s=("ababcbacadefegdehijhkkkli")
print(partitionLabels(s))



