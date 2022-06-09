'''
print(animal[0],animal[-1],animal[2:10:2])
print(animal[:-1],animal[-1])
print(animal[::-1])
'''

animal = [ 'rat', "ox", "tiger", "rabbit",
           'dragon', 'snake', 'horse', 'goat',
           'monkey', 'rooster', 'dog', 'pig']

print(animal[0][0])

animal_leg = []
animal_leg.append(0)
animal_leg.append(animal[0])
print(animal_leg)

animal_head = []
for item in animal:
    if item[0] == 'r':
        animal_head.append(item)
print(animal_head)

