def confirmEnding(text,target):
    
    len_tar = len(target)
    endi = text[-len_tar:]
    return target == endi

tex = 'If you want to save our world, you must hurry. We dont know how much longer we can withstand the nothing'
tar = 'othing'

sol = confirmEnding(tex,tar)

if sol:
    print('\nTHE TEXT "', tex,'" ENDS IN "', tar, '"')
else:
    print('\nTHE TEXT "', tex,'" DOES NOT END IN "', tar, '"')