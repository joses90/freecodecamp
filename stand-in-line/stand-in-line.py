def nextInLine(arr, item):
    if len(arr) > 0:
        remov = arr[0]
        del arr[0]
    else:
        remov = 'None'
    arr.append(item)
    return arr, remov

testArr = [5, 6, 7, 8, 9]
new = 1

print('\nBefore: ', testArr)
print('New number: ', new)
arr_sol, item_sol = nextInLine(testArr, new)
print('After: ', arr_sol)
print('Removed: ', item_sol)