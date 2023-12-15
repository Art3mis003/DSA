def BalancedSum(array):
    l = 0
    r = sum(array)
    for i in range(len(array)):
        r -= array[i]
        if l == r:
            return i
        l += array[i]
    return -1

array=[1,2,3,4,6]
print(BalancedSum(array))