def gasStations(gas,cost):
    start=0
    totalGas=0
    currGas=0
    for i in range(len(gas)):
        totalGas+= gas[i]-cost[i]
        currGas+=gas[i]-cost[i]

        if currGas<0:
            start=i+1
            currGas=0
    return start if totalGas>=0 else -1


gas=[2,2,3,4,5]
cost=[3,4,2,1,2]
print(gasStations(gas,cost))
