def factorialize(num):
    
    if type(num) == int:
        # If number is 0 or 1, return 1
        if (num == 0 or num == 1):
            sol = 1
        # Else, the result should be the number times the number-1
        # This function is recursive and calls itself for the previous number
        else:
            sol = num * factorialize(num-1)

    return sol

num = 10
sol = factorialize(num)

# Check if the number provided is an integer
if type(num) == int:
    print('\nThe factorial of', num, 'is', sol)
# If it is not an integer, it will print a message saying so
else:
    print('\nNumber', num,'is not an integer')