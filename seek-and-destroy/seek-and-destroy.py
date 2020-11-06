def destroyer(arr, args):
    arr_new = []
    
    for i in arr:
        if i not in args:
            arr_new.append(i)
    return arr_new

arr = ['possum', 'trollo', 12, 'safari', 'hotdog', 92, 65, 'grandma',
       'bugati', 'trojan', 'yacht']
argu = ['yacht', 'possum', 'trollo', 'safari', 'hotdog', 'grandma',
        'bugati', 'trojan']
sol = destroyer(arr, argu)
print('\nThe array', arr, 'without the elements', argu,'is', sol)