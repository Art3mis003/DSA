def topkfreq(nums, k):
    count= {}
    frequency=[[] for i in range (len(nums)+1)]
    for n in nums:
        count[n]= 1+ count.get(n,0)
    for num , c in count.items():
        frequency[c].append(num)
    answer=[]
    for i in range(len(frequency)-1,0,-1):
        for n in frequency[i]:
            answer.append(n)
            if len(answer)==k:
                return answer


array= [78,90,78,65,45,65]
ans=topkfreq(array,2)
for i in ans:
    print (i)





