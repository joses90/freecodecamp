def mutation(arr):
    # Store each word in a different variable and lowercase them
    word1 = arr[0].lower()
    word2 = arr[1].lower()
    
    # Initialise the count of letters in the 2nd word that are in the 1st
    result = 0
    l = len(word2)
    
    # Loop through the letters of the 2nd word
    for i in range(l):
        # Check if the current letter in the 1st word is in the 2nd
        if word2[i] in word1:
            # If it is, increase the counter by 1
            result = result + 1
            
    # Compare if the amount of letters in the 2nd word equal the counter
    return result == l

arr = ['Noel', 'Ole']
sol = mutation(arr)
print(
      '\nDoes the first word contain all of the letters of the second word?',
      sol)