'''
https://brilliant.org/daily-problems/tough-choices/
Malina has been invited to Brilliant Taste, the fanciest restaurant
in town. She has to pick one starter out of three
(fish, meat, and vegetarian), one main out of five
(two fish, two meat, and one vegetarian), and one dessert out of two
(chocolate and fruit).

She wants at most one fish plate. Also, if she chooses at least one
vegetarian option, then she'll take chocolate for dessert for sure.
How many options is she left with?

13,19,20,26
Submit
'''

starter = ['fish', 'meat', 'vegetarian']
main = ['fish', 'fish','meat', 'meat','vegetarian']
dessert = ['chocolate','fruit']

# She pick ONE of starter,wants at most one fish plate.
# Also pick ONE of main, if she chooses at least one vegetarian option,
# then she'll take chocolate for dessert for sure.
# How many options is she left with?

cunt,cuntall = 0,0
menu = []
for i in starter:
    for j in main:
        #menu.append([i,j])
        for k in dessert:
            cuntall += 1
            if [i,j,k].count('fish') <= 1 and [i,j,k].count('vegetarian')>=1 and [i,j,k].count('chocolate')==1:
                menu.append([i,j])
                cunt += 1
print(cuntall - cunt,menu)


from itertools import product

meals = product(["f", "m", "v"], ["f", "f", "m", "m", "v"], ["c", "fr"])

options = 0
for meal in meals:
  if meal.count("f") <= 1:
    if "v" in meal and "c" in meal or "v" not in meal:
      options += 1

print(options)


