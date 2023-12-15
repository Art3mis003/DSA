def longestSubstr(s):
    l=0
    map=set()
    res=0

    for r in range(len(s)):
        while s[r] in map:
            map.remove(s[l])
            l+=1

        map.add(s[r])
        res= max(res,r-l+1)

    return res

s="abdefgabef"
print(longestSubstr(s))
