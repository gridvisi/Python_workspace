'''
https://www.geeksforgeeks.org/python-string-translate/?ref=rp

string.translate(mapping)

mapping – a dictionary having mapping between two characters.
Returns : Returns modified string where each character is mapped to
its corresponding character according to the provided mapping table.

string.translate(mapping)
mapping - 具有两个字符之间的映射的字典。
返回。返回经过修改的字符串，其中每个字符都根据提供的映射表被映射到相应的字符上。
'''
# 恺撒密码
# Python3 code to demonstrate
# translations without
# maketrans()
# specifying the mapping
# using ASCII

# target string
trg = "life is short"
ascTrg = [ord(c) for c in trg]
print(ascTrg)
codkey = [i+7 for i in ascTrg]

key = [i for i in range(len(trg))]
codKey = [x-y for x,y in zip(ascTrg,key)]
print(codKey)
table = dict(zip(ascTrg,codKey))

# Printing original string
print("The string before translating is : ", end="")
print(trg)
print(trg.translate(table))
s = trg.translate(table)
#decode
#s = 'lddbdkk_egh'
ascTrg = [ord(c) for c in s]
key = [i for i in range(len(ascTrg))]
codKey = [x+y for x,y in zip(ascTrg,key)]
print(codKey)
table = dict(zip(ascTrg,codKey))
print("The string before translating is : ", end="")
#print(s)
print(s.translate(table))



# pi
# Mathematical Functions in Python | Set 3 (Trigonometric and Angular Functions)
# Python code to demonstrate the working of
# sin() and cos()

# importing "math" for mathematical operations
import math

a = math.pi / 6

# returning the value of sine of pi/6
print("The value of sine of pi/6 is : ", end="")
print(math.sin(a))

# returning the value of cosine of pi/6
print("The value of cosine of pi/6 is : ", end="")
print(math.cos(a))





# Python3 code to demonstrate
# translations without
# maketrans()

# specifying the mapping
# using ASCII
table = {119: 103, 121: 102, 117: None}

# target string
trg = "weeksyourweeks"

# Printing original string
print("The string before translating is : ", end="")
print(trg)

# using translate() to make translations.
print("The string after translating is : ", end="")
print(trg.translate(table))

# Python 3 Program to show working
# of translate() method

# specifying the mapping
# using ASCII
translation = {103: None, 101: None, 101: None}

string = "geeks"
print("Original string:", string)

# translate string
print("Translated string:",
      string.translate(translation))

# Python 3 Program to show working
# of translate() method

# First String
firstString = "gef"

# Second String
secondString = "eks"

# Third String
thirdString = "ge"

# Original String
string = "geeks"
print("Original string:", string)

translation = string.maketrans(firstString,
                               secondString,
                               thirdString)

# Translated String
print("Translated string:",
      string.translate(translation))