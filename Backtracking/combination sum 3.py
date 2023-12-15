def combSum3(n, k):
    res = []

    def comb(i, dummy, k, total):
        if total == n and k == 0:
            res.append(dummy[:])
            return

        if k == 0 or total >= n or i > 9:
            return


        dummy.append(i)
        comb(i + 1, dummy, k - 1, total + i)
        dummy.pop()
        comb(i+1,dummy,k,total)
        
    comb(1, [], k, 0)  # Start with 1, as numbers in the range are from 1 to 9
    return res

n = 9
k = 3
print(combSum3(n, k))

