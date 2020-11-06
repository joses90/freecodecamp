def rangeOfNumbers(startNum, endNum):

    if startNum == endNum:
        return [startNum]
    else:
        num = rangeOfNumbers(startNum, endNum-1)
        num.append(endNum)
        return num

startNum = 3
endNum = 10
if startNum <= endNum:
    sol = rangeOfNumbers(startNum, endNum)
    print('\nThe numbers going from', startNum,'and', endNum, 'are', sol)
else:
    print('\nNumber', startNum,'is not lower or equal than', endNum)