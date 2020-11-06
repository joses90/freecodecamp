# Import others
import sortarray as sa
import find_position as fp
import insert_number as inu

# Values
arr = [43,19.1,3,5,100,18.9,-6,0,-22]
n = 19
print('\nThe array is:\t\t',arr)

# Sort list
arr_sort = sa.sortarray(arr)
print('The sorted array is:\t\t', arr_sort)

# Find the position
p = fp.findposition(arr_sort,n)
print('The position for number', n,'is:\t', p)

# Insert the number
arr_fin = inu.insertnumber(arr_sort,n,p)
print('The new array is:\t\t', arr_fin)
