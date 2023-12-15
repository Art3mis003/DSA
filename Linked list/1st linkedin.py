
def minTime(word):
    ans = 0
    curr = 0

    for i in range(len(word)):
        k = ord(word[i]) - ord('A')
        ans += min(abs(k - curr), 26 - abs(k - curr))
        curr = k
    return ans

wors="AZGB"
print(minTime(wors))