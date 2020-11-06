import pandas as pd
import numpy as np

def lookUpProfile(name, prop):
    # Reads a csv file and returns the value for a contact
    # if it finds it in the file and different messages if it
    # does not find the contact or column
    
    df = pd.read_csv('profiles.csv')
    name_is = (df['firstName'] == name).any()
    if name_is:
        prop_is = (df.columns == prop).any()
        if prop_is:
            result = df.loc[df['firstName'] == name, prop].iloc[0]
        else:
            result = 'No such property'
    else:
        result = 'No such contact'
    return result

tests =[['Kristian','lastName'],
        ['Sherlock','likes'],
        ['Harry', 'likes'],
        ['Bob','number'],
        ['Bob', 'potato'],
        ['Akira', 'address']]
l = tests[0][0]
l2 = len(tests)
for i in range(len(tests)):
    j = tests[i][0]
    k = tests[i][1]
    solution = lookUpProfile(tests[i][0],tests[i][1])
    print('\nName:', tests[i][0])
    print('Column:', tests[i][1])
    print('\nRESULT:', solution)
    
print('\n###################################')
print('\nTESTS FINISHED')
print('\n###################################')