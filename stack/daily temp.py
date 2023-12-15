def dailyTemp(nums):
    stack=[]
    result=[0]* len(nums)
    for i, t in enumerate(nums):
        while stack and t> stack[-1][0]: #as we are accessing top of the stack
              stackT , stackInd = stack.pop()# and it's 0th index tupple element.
              result[stackInd]= i-stackInd
        stack.append((t,i))
    return result

