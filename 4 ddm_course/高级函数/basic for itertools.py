#https://florian-dahlitz.de/blog/introduction-to-itertools
#https://pymotw.com/3/itertools/index.html#combining-inputs
#https://github.com/more-itertools/more-itertools
#https://docs.python.org/3/library/itertools.html

# below code source from this:
#https://github.com/DahlitzFlorian/article-introduction-to-itertools-snippets/
from itertools import count
c = count()
for i in range(5):
    print(next(c))

c = count(10, 2)
for i in range(5):
    print(next(c))

names = ["Alice", "Bob", "Larry", "Margaret"]
names_with_index = [name for name in zip(count(1), names)]
print(names_with_index)


#itertools_cycle.py
from itertools import cycle

names = ["Alice", "Bob", "Chris", "Larry", "Margaret", "Naomi", "Sarah"]
groups = cycle([1, 2, 3])
names_with_groups = [name for name in zip(names, groups)]
print(names_with_groups)

from itertools import repeat
print(list(map(pow, range(10), repeat(3))))
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

from itertools import chain
class1 = ["Alice", "Bob", "Chris"]
class2 = ["Larry", "Margaret", "Naomi", "Sarah"]
all_people = list(chain(class1, class2))
print(f"All people: {all_people}")

# itertools_compress.py

from itertools import compress
def name_selection(names):
    name_selectors = []

    for name in names:
        if name.startswith("A"):
            name_selectors.append(1)
        else:
            name_selectors.append(0)
    return name_selectors

names = ["Albert", "Alexandra", "Miriam", "Sascha"]
filtered_names = list(compress(names, name_selection(names)))
print(f"Filtered names: {filtered_names}")

#dropwhile
from itertools import dropwhile
print(list(dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1])))

from itertools import takewhile
print(list(takewhile(lambda x: x < 5, [1, 4, 6, 4, 1])))

# itertools_filterfalse.py
from itertools import filterfalse

def is_negative(number):
    return number < 0

numbers = [-1, 0, 4, 1, -3]
positive_numbers = list(filterfalse(is_negative, numbers))
print(positive_numbers)

# itertools_groupby.py

from itertools import groupby
from operator import itemgetter

data = [
    (0, 0),
    (0, 1),
    (1, 4),
    (0, 9),
    (1, 2),
    (2, 5),
    (1, 6),
]

for k, v in groupby(data, itemgetter(0)):
    print(k, list(v))

# itertools_islice.py

from itertools import islice

list1 = list(islice(range(50), 2))
list2 = list(islice(range(50), 40, 44))
list3 = list(islice(range(50), 5, 45, 10))

print(f"islice with stop parameter only: {list1}")
print(f"islice with start and stop: {list2}")
print(f"islice with start, stop, and step: {list3}")

# itertools_starmap.py

from itertools import starmap
def pow_with_input(base, exponent):
    return base, exponent, pow(base, exponent)
values = [(4, 9), (1, 6), (0, 5), (3, 8), (2, 7)]
for i in starmap(pow_with_input, values):
    print("pow({}, {}) = {}".format(*i))
#pow(4, 9) = 262144
#pow(1, 6) = 1
#pow(0, 5) = 0
#pow(3, 8) = 6561
#pow(2, 7) = 128

# itertools_tee.py

from itertools import islice
from itertools import tee

s = islice(range(100), 5)
s1, s2 = tee(s)

print(f"First list: {list(s1)}")
print(f"Second list: {list(s2)}")


# itertools_zip_longest.py

from itertools import zip_longest
a = [1, 2, 3]
b = ["One", "Two"]
result1 = list(zip(a, b))
result2 = list(zip_longest(a, b))
print(result1)
print(result2)
#[(1, 'One'), (2, 'Two')]
#[(1, 'One'), (2, 'Two'), (3, None)]


# accumulate
from itertools import accumulate
from operator import mul

numbers = [1, 2, 3, 4, 5]
result1 = accumulate(numbers)
result2 = accumulate(numbers, mul)
result3 = accumulate(numbers, initial=100)

print(f"Result 1: {list(result1)}")
print(f"Result 2: {list(result2)}")
print(f"Result 3: {list(result3)}")


# itertools_product.py

from itertools import chain
from itertools import product

FACE_CARDS = ("J", "Q", "K", "A")
SUITS = ("H", "D", "C", "S")

DECK = list(
    product(
        chain(range(2, 11), FACE_CARDS),
        SUITS,
    )
)
print(DECK)
for card in DECK:
    print("{:>2}{}".format(*card), end=" ")
    if card[1] == SUITS[-1]:
        print()

# itertools_permutations.py

from itertools import permutations

l = [1, 2, 3]
result1 = list(permutations(l))
result2 = list(permutations(l, 2))

print(result1)
print(result2)

# itertools_combinations.py

from itertools import combinations

l = [1, 2, 3]
m = [1 , 2, 3, 1]
result1 = list(combinations(l, 3))
result2 = list(combinations(l, 2))
result3 = list(combinations(m, 3))

print(result1)
print(result2)
print(result3)

#the combinations_with_replacement() function
#does compute combinations which include repeated elements.
# itertools_combinations_with_replacement.py

from itertools import combinations_with_replacement

l = [1, 2, 3]
result1 = list(combinations_with_replacement(l, 3))
result2 = list(combinations_with_replacement(l, 2))

print(result1)
print(result2)

#Now, you can use functions like flatten():
# more_itertools_flatten.py

from more_itertools import flatten

nested_list = [[1, 2], [3, 4]]
flattened_list = list(flatten(nested_list))

print(flattened_list)


def marsExploration(s):
    sos = cycle('SOS')
    bit_flips = 0
    for letter in s:
        if letter != next(sos):
            bit_flips += 1
    return bit_flips
s = 'eric'
print(marsExploration(s))