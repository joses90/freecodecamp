def largestofFour(arr):
    res = []
    for row in arr:
        res.append(max(row))
    return res;

example = [[17, 23, 25, 12], [25, 7, 34, 48], [4, -10, 18, 21], [-72, -3, -17, -10]]
sol = largestofFour(example)
print('\nThe largest numbers in each row are:', sol)