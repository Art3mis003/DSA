def isAnagram(s, t) -> bool:
    if len(s) != len(t):
        return False

    countS, countF = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countF[t[i]] = 1 + countF.get(t[i], 0)

    for c in countS:
        if countS[c] != countF.get(c, 0):
            return False
    return True


s="OKjaanu"
t="jaanuOK"
isAnagram(s,t)