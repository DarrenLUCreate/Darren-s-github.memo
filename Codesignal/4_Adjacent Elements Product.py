def adjacentElementsProduct(inputArray):
    finalArray = []
    for i in range(len(inputArray)-1):
        finalArray.append(inputArray[i]*inputArray[i+1])
    result = max(finalArray)
    return result
    
