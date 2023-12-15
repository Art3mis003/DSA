def buyAndSell(prices):

    res=0
    l = prices[0]

    for price in prices:
        if price < l:
            l=price
        res=max(res, price-l)
    return res



prices=[52,56,98,121,45,90]
print(buyAndSell(prices))