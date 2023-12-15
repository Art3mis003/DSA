def combsum2(arr,t):
    res=[]
    ds=[]
    def dfs(i,total):
        if total==t:
            res.append(ds[:])
            return
        if i>=len(arr) or total>t:
            return
        ds.append(arr[i])
        dfs(i+1,total+arr[i])
        ds.pop()
        dfs(i+1,total)
    dfs(0,0)
    return res

arr=[1,2,3,4,5]
t=5
print(combsum2(arr,t))