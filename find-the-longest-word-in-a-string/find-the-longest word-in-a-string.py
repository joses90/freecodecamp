def findLongestWordLength(string):
    leng = 0
    word = ''
    lis = string.split()
    for w in lis:
        if len(w) > leng:
            leng = len(w)
            word = w
    return word, leng

text = 'What is the average airspeed velocity of an unladen swallow'
w,c = findLongestWordLength(text)
print('\nThe longest word is', w, 'where the length is', c, 'characters.')