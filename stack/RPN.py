def rPn(s):
    stack=[]
    for c in s:
        if c=="+":
            stack.append(stack.pop()+stack.pop())
        elif c=="*":
            stack.append(stack.pop()*stack.pop())
        elif c=="/":
            a,n= stack.pop(), stack.pop()
            stack.append(int(n/a))
        elif c=="-":
            a,n= stack.pop(),stack.pop()
            stack.append(n-a)
        else:
            stack.append(int(c))
    return stack[0]

# s=['12',"1",'6','*','/']
# print(rPn(s))

array=[1,2,3,4,5,6,7,8,9,10]
for i,n in enumerate(array):
    print(i,n)