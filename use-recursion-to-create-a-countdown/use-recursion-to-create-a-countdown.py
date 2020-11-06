def countdown(n):

    if n == 1:
        return [n]
    else:
        num = countdown(n-1)
        num.insert(0,n)
        return num

n = 10
if n >= 1:
    sol = countdown(n)
    print('\nThe countdown from', n,'is', sol)
else:
    print('\nNumber', n,'is not greater or equal than 1')