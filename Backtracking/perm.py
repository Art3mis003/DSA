def perm(nums):
    res=[]
    map={}
    for val in nums:
        map[val]=0

    def dfs(curr,map):
        if len(curr)==len(nums):
            res.append(curr[:])
            return
        for val in map:
            if map[val]==0:
                map[val]=1
                curr.append(val)
                dfs(curr,map)
                map[val]=0
                curr.pop()
    dfs([],map)
    return res

nums=[1,2,3]
print(perm(nums))
