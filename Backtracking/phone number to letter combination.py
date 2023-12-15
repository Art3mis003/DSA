def phoneToChar(digits):
    res=[]
    map={'2':'abc', '3':'def',
         '4':'ghi','5':'jkl','6':'mno','7':'pqrs',
         '8':'tuv','9':'wxyz'}

    def dfs(i,curs):
        if len(curs)==len(digits):
            return res.append(curs)
        for c in map[digits[i]]:
            dfs(i+1,curs+c)
    if not digits:
        return []
    dfs(0,'')
    return res

digits="93"
print(phoneToChar(digits))


