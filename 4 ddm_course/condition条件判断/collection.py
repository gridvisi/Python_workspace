
from collections import Counter

cheese = ["gouda", "brie", "feta", "cream cheese", "feta", "cheddar",
          "parmesan", "parmesan", "cheddar", "mozzarella", "cheddar", "gouda",
          "parmesan", "camembert", "emmental", "camembert", "parmesan"]

person = ["rat", "rabbit", "dog", "dragon", "rat", "tiger","rat","duck",
          "dragon", "camel", "snake", "bee", "chicken", "dog","pig",
          "cat", "cat", "rabbit", "horse", "pig"]

cheese_count = Counter(person)
print(cheese_count.most_common(3))
# Prints: [('rat', 3), ('rabbit', 2), ('dog', 2)]
print(cheese_count.most_common(5))

#[('rat', 3), ('rabbit', 2), ('dog', 2), ('pig', 2), ('cat', 2)]
#Under the hood, Counter is just a dictionary that maps items to number of occurrences,
# therefore you can use it as normal dict:

print(cheese_count["dog"])
cheese_count["rat"] += 1
print(cheese_count["rat"])

print(ord('U'))
shift = ord('A') - ord('U')
shift = ord('u') - ord('a')
print('shift:',shift)

print(ord('b'))
print(chr(98+20))
j = ''
for i in 'lcx':
    j = j + chr(ord(i) - shift + 7)
print('mark:',j)

solo,both = [],[]
apply_math = ["peter parker", "susan", "jack",  "kevin", "summer", "steve", "mcree"]
apply_code = ["lily", "lucy", "jack", "alex", "emma", "summer", "steven", "susie"]
for person in apply_math:
    if person in apply_code:
        both.append(person)
    else:
        solo.append(person)
print('solo&both:',solo,both)
