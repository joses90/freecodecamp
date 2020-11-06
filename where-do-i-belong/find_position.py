def findposition(arr, num):
    
    i = 0
    pos = -1
    
    while (i <= len(arr) and pos == -1):
        if  arr == []:
            pos = 0
        elif num <= arr[i]:
            pos = i
        i = i+1
    
    return pos