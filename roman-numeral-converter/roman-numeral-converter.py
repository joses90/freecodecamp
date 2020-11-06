def convertToRoman(num):
    if num < 4000:
        res = ''
        lis = [int(d) for d in str(num)]
        lis.reverse()
        h = len(lis)
        for i in range(h):
            if i == 0:
                if lis[i] in (1,2,3):
                    res = lis[i]*'I'
                elif lis[i] == 4:
                    res = 'IV'
                elif lis[i] in (5,6,7,8):
                    res = 'V' + (lis[i] - 5)*'I'
                elif lis[i] == 9:
                    res = 'IX'
            elif i == 1:
                if lis[i] in (1,2,3):
                    res = lis[i]*'X' + res
                elif lis[i] == 4:
                    res = 'XL' + res
                elif lis[i] in (5,6,7,8):
                    res = 'L' + (lis[i] - 5)*'X' + res
                elif lis[i] == 9:
                    res = 'XC' + res
            elif i == 2:
                if lis[i] in (1,2,3):
                    res = lis[i]*'C' + res
                elif lis[i] == 4:
                    res = 'CD' + res
                elif lis[i] in (5,6,7,8):
                    res = 'D' + (lis[i] - 5)*'C' + res
                elif lis[i] == 9:
                    res = 'CM' + res
            elif i == 3:
                if lis[i] in (1,2,3):
                    res = lis[i]*'M' + res
    else:
        res = 'ERROR, number is larger than 3999'
    return res

num = 3999
rom = convertToRoman(num)
print('\nThe number', num, 'in roman numerals is', rom)
# 3999 is MMMCMCXIX