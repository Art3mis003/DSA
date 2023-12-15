def climbstairs(n):
    prev=1
    prev2=1
    curr=1
    for i in range(2,n+1):
        curr=prev+prev2
        prev2=prev
        prev=curr
    return curr
n=4
print(climbstairs(n))
