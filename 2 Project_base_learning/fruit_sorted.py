'''
fruit = ['apple','banana','carrot','dates','fig','grape','kiwi','lemon']
print(sorted(fruit))
print(sorted(fruit,reverse=True))
print(sorted(fruit,key=lambda x:x[0]))
print(sorted(fruit,key=lambda x:x[1]))

prices = [10,3,2,7,5,9,13,8]

fruit_price_sheet = dict(zip(fruit,prices))
print(fruit_price_sheet)
print(sorted(fruit_price_sheet))

fps = fruit_price_sheet
print(sorted([k for k,v in fps.items()],key=fps.get))
print(sorted(fps.items(),key=lambda x:x[1]))

#print(sorted(fps.items(),key=fps.get))
#print([v for v in sorted(fruit_price_sheet.values())])
#print(sorted(fruit_price_sheet.items(), lambda x, y: cmp(x[1], y[1])))
'''

fruit_cal= {'Grapefruit':36,
            'Orange':47,
            'Pinneapple':55,
            'Coconut':352,
            'Apple':48,
            'Avocado':197,
            'kiwi':56,
            'Pear':54,
            'Peach':43,
            'Blackberry':44,
            'Strawberry':41,
            'Raspberry':34
            }

fruit_price = {'Grapefruit':15,
            'Orange':8,
            'Pinneapple':6,
            'Coconut':7,
            'Apple':17,
            'Avocado':20,
            'kiwi':35,
            'Pear':5,
            'Peach':16,
            'Blackberry':40,
            'Strawberry':30,
            'Raspberry':130
            }

class Fruit:
     def __init__(self, name, cal, price):
         self.name = name
         self.cal = cal
         self.price = price
     def __repr__(self):
         return repr((self.name, self.cal, self.price))

sheet = [(k,v,fruit_price[k]) for k,v in fruit_cal.items()]
print(sorted(sheet, key=lambda x: x[1]))
fruit_objects = [Fruit(i[0],i[1],i[2]) for i in sheet]

#print(fruit_objects)
print(sorted(fruit_objects, key=lambda fruit: fruit.cal))   # sort by price#
print(sorted(fruit_objects, key=lambda fruit: fruit.price))
print(sorted(fruit_objects, key=lambda fruit: (fruit.cal,fruit.price)))
