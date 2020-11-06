def insertnumber(arr,num,pos):
    
    arr_f = arr[:]
    arr_f.sort()
    
    arr_f.insert(pos,num)
    
    return arr_f