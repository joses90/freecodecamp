def palindrome(string):
    
    # Turn string to lowercase
    text = string.lower()
    # Remove everything that is not a letter or a number:
    #   Lowercase letters are ascii 97 to 122
    #   Numbers are ascii 48 to 57
    new_text = ''
    for i in range(len(text)):
        char = text[i]
        if ((ord(char) in range(48,57+1)) | (ord(char) in range(97,122+1))):
            new_text = new_text + char
    #Check if it is a palindrome
    inv = new_text[::-1]
    return (inv == new_text)

text = 'five|\_/|four'
sol = palindrome(text)

if sol == True:
    print(text, 'IS A PALINDROME')
else:
    print(text, 'IS NOT A PALINDROME')