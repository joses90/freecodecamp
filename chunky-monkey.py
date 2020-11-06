def chunkArrayinGroups(arr,size):
    arr_new = []
    chunk = []
    l = len(arr)
    # Loop once per beginning of new chunk
    for i in range(0, l, size):
        # Loop through new chunk
        for j in range(i, i+size):
            # Update current chunk unless it is the last part and the length
            # will be exceeded
            if j < l:
                chunk.append(arr[j])
        # Update solution with current chunk
        arr_new.append(chunk)
        # Reset chunk variable to use it again
        chunk = []
    return arr_new

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
size = 2
sol = chunkArrayinGroups(arr, size)
print('\nOriginal array:\t', arr)
print('Length of groups:\t', size)
print('\nSplit array:\t', sol)
