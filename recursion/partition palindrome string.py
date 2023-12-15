def palindromePart(s):
    res=[]
    def palindrome(s,f , last):
        while f <= last:
            if s[f] != s[last]:
                return False
            f += 1
            last -= 1
        return True
    def part(path,ind):
        if ind==len(s):
            return res.append(path[:])
        for i in range(ind,len(s)):
            if palindrome(s,ind,i):
                path.append(s[ind:i+1])
                print(s[ind:i])
                part(path,i+1)
                path.pop()
    part([],0)
    return res



s="aab"
print(palindromePart(s))
