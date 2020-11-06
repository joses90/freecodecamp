import numpy as np

def multiplyAll(arr):
    # Initialise variables
    result = 1
    i = 0
    
    # Convert list into numpy array and find the number of rows
    array = np.array(arr, dtype = object)
    siz = np.shape(array)
    
    # One row at a time
    while (i < siz[0]):
        # Find the number of columns for the current row
        row_l = len(array[i])
        # One column (number) at a time
        for j in range(row_l):
            # Mutiply the temporary result by the current number
            result = result * array[i][j]
        # Update number of row
        i = i + 1
    
    return result

arr = [[5,1],[0.2, 4, 0.5],[3, 9]]
sol = multiplyAll(arr)
print('\nThe product of all numbers in', arr,'is',sol)