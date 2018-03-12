# Returns: the unweighted ECN of one price for one specific set of denominations
# Inputs: takes 4 denominations, a price, and the ECN array
def computeECN(array, price, deno1, deno2, deno3, deno4):
    ecn1 = array[price - 1 - deno1] + 1
    ecn2 = array[price - 1 - deno2] + 1
    ecn3 = array[price - 1 - deno3] + 1
    ecn4 = array[price - 1 - deno4] + 1

    ecnsArray = [ecn1, ecn2, ecn3, ecn4]
    finalECN = ecn1

    if price > deno4:
        finalECN = findMinECN(ecnsArray)
    elif (price > deno3) and (price < deno4):
        finalECN = findMinECN(ecnsArray[0:3])
    elif (price > deno2) and (price < deno3):
        finalECN = findMinECN(ecnsArray[0:2])
    elif (price > deno1) and (price < deno2):
        finalECN = ecn1
    else:
    	finalECN = 1
    return finalECN

# Returns: the minimum element in a specified array
# Inputs: array
def findMinECN(array):
    minECN = array[0]
    for i in range(0, len(array), 1):
        if array[i] < minECN:
            minECN = array[i]
    return minECN

# Returns: the sum of all the elements in an array
# Inputs: array
def computeSumOfECN(array):
    sum = 0
    for i in range(0, len(array), 1):
        sum += array[i]
    return sum

n = input("What is the value of N? ")
n = int(n)
den1 = 1
den2 = 2
den3 = 3
den4 = 4
bestDen1 = den1
bestDen2 = den2
bestDen3 = den3
bestDen4 = den4

ECNArray = [0] * 239
ECNArray[0] = 1

minIntTotal = 9223372036854775807

# For all set of denominations ...
for den2 in range(2, 11, 1):
    ECNArray[den2 - 1] = 1
    for den3 in range(den2+1, 51, 1):
        ECNArray[den3 - 1] = 1
        for den4 in range(den3+1, 102, 1):
            ECNArray[den4 - 1] = 1
            # ... computes the unweighted ECN of each price
            for price in range(1, 240, 1):
                ECNArray[price - 1] = computeECN(ECNArray, price, den1, den2, den3, den4)
            # ... computes the weighted ECN of prices that are multiples of 5
            for price in range(1, 240, 1):
                if (price%5) == 0:
                    ECNArray[price - 1] *= n
            # finds the most optimal set of denominations
            if computeSumOfECN(ECNArray) < minIntTotal:
                bestDen2 = den2
                bestDen3 = den3
                bestDen4 = den4
                minIntTotal = computeSumOfECN(ECNArray)

# Computes the ECNs of the prices using the best denominations
bestArray = [0] * 239
for price in range(1, 240, 1):
    bestArray[price - 1] = computeECN(bestArray, price, bestDen1, bestDen2, bestDen3, bestDen4)
for price2 in range(1, 240, 1):
    if (price%5) == 0:
        bestArray[price2 - 1] *= n

# Displays the best array
for i in range(0,len(bestArray),1):
    prices = [0] * 239
    for j in range(0, len(prices), 1):
        prices[j] = j + 1
    print(str(prices[i]) + str("\t") + str(bestArray[i]))

print("The best denominations are: " + str(den1) + ", " + str(bestDen2) + ", " + str(bestDen3) + ", " + str(bestDen4))
print("The lowest total is: " + str(minIntTotal))
