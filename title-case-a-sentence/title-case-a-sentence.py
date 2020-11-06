def titleCase(text):
    # Lowercasing the whole sentence
    result = text.lower()
    # Dividing the sentence into words into a list
    list_words = result.split()
    # Initialising the final string result
    capi = ''
    # Looking word for word
    for word in list_words:
        # Capitalising the first character of every word
        r = word.capitalize()
        # Updating the word and adding a space before the next word
        capi = capi + r + ' '
    # Removing the unnecesary space at the end of the sentence
    capi = capi[:-1]
    return capi

# Testing different texts to check the solution
text = 'I\'m a little tea pot'
sol = titleCase(text)
print('\nOriginal text: ', text)
print('Modified text: ', sol)

text2 = 'sHoRt AnD sToUt'
sol2 = titleCase(text2)
print('\nOriginal text: ', text2)
print('Modified text: ', sol2)

text3 = 'HERE IS MY HANDLE HERE IS MY SPOUT'
sol3 = titleCase(text3)
print('\nOriginal text: ', text3)
print('Modified text: ', sol3)