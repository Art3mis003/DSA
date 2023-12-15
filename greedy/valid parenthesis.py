def validPaarenthesis(s):
    maxOpen,minOpen=0,0

    for c in s:
        if c=='(':
            maxOpen+=1
            minOpen+=1
        elif c==')':
            minOpen=max(0,minOpen-1)
            maxOpen-=1
        elif c=='*':
            minOpen=max(0,minOpen-1)
            maxOpen+=1

        if maxOpen<0:
            return False

    return True if minOpen==0 else False

s="(**))"
print(validPaarenthesis(s))