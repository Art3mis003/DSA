def longestChar(s, k):
    res = 0
    count = {}  # count of each char hence a dict
    l = 0
    for r in range(len(s)):  # r is the right pointer and l is the left pointer of the window
        count[s[r]] = 1 + count.get(s[r],0)  # * count of each char using get method as it returns 0 if the char is not present in the dict *#
        if (r - l + 1) - max(count.values()) > k: # if the window size - max count of any char in the window is greater than k
            count[s[l]] -= 1 # decrement the count of the char at the left pointer
            l += 1 # increment the left pointer
        res = max(res, r - l + 1) # update the res
    return res


s = "aabccbb"
k = 2
print(longestChar(s, k))
