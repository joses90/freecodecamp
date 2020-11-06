sol = 0

def cc(card):
    val = 0
    if card in range(2,7):
        val = 1
    elif card in range(7,10):
        card
    else:
        val = -1
    
    return val

inp = ''
shown = []

while (inp != 'end'):
    card = input('New card: ')
    if card in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
        shown.append(card)
        card = int(card)
        sol = sol + cc(card)
    elif card in ['J','Q','K','A']:
        shown.append(card)
        sol = sol + cc(card)
    elif card == 'end':
        inp = card
    else:
        print('Wrong input, try a real card value')
        
if sol > 0:
    sol = str(sol) + ' Bet'
else:
    sol = str(sol) + ' Hold'

print('\nCards Sequence ', end = '')
print(*shown, sep = ', ', end = '')
print(' should return', sol)
