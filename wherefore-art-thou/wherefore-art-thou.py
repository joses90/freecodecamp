class Person():
    
    def __init__(self, first, last):
        self.first = first
        self.last = last       
        self.fir_att = 'first'
        self.las_att = 'last'

# PENDING TO TEST __getattribute__

def whatIsInAName(collection, source):
    
    title = list(source.keys())[0]
    value = sou[title]
    res = []
    
    # List of attributes for class Person
    att = dir(collection[0])
    # h = 1 if title is one of the attributes
    k = 0
    if title in att:
        h = 1
        for i in range(len(collection)):
            firs = (collection[i].fir_att == title and collection[i].first == value)
            las = (collection[i].las_att == title and collection[i].last == value)
            if firs or las:
                res.append(vars(collection[i]))
                k = 1
    else:
        h = 0

    return res, h, k

coll = [Person('Romeo','Montague'),
        Person('Mercutio', 'NULL'),
        Person('Tybalt', 'Capulet'),
        Person('Juliet', 'Capulet')]
sou = {'last': 'Capulet'}

sol, ti, va = whatIsInAName(coll, sou)

if ti == 1 and va == 1:
    for i in range(len(sol)):
        print('\nFirstname:\t', sol[i]['first'])
        print('Surname:\t', sol[i]['last'])
elif ti == 0:
    print('\nThe title', list(sou.keys())[0],'is not in the collection')
else:
    print('\nThe person', sou[list(sou.keys())[0]],'is not in the collection')
