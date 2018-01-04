# -*- coding: utf-8 -*-

people = int(input('Enter number of people: '))
billTotal = float(input('Enter bill amount before tax and tip: '))
tip = int(input('Enter a tip percentage: '))
tax = int(input('Enter a tax percentage: '))
#items = input('Enter item: ')


# should be able to say 5 beers person1 has 2 person 4 had 1 and person3 had 1


if input('Split it evenly? Y/N  : ') == 'Y':
    split = ((billTotal/people) * (1 + tax/100) )* (1 + tip/100)
    print('$' + str(round(split, 1)))

else:
    count = 0
    list = []
    while count < people:
        value = int(input ('Person ' + str(count) + ' total: '))
        list.append[value]        
    for i in list:
        print('Person' + i + ' owes: ' + str(list[i]))


## not working yet
    count2 = 0
    while count < people:
        dict ['person' + str(count) ] = int(input ('Person ' + str(count) + ' total: '))
        count += 1        
    for k, v in dict.items():
        print(k, v)
