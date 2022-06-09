
#https://www.geeksforgeeks.org/python-maketrans-translate-functions/

# Python3 code to demonstrate
# translations using
# maketrans() and translate()

# specify to translate chars
str1 = "wy"

# specify to replace with
str2 = "gf"

# delete chars
str3 = "u"

# target string
trg = "weeksyourweeks"

# using maketrans() to
# construct translate
# table
table = trg.maketrans(str1, str2, str3)

# Printing original string
print("The string before translating is : ", end="")
print(trg)

# using translate() to make translations.
print("The string after translating is : ", end="")
print(trg.translate(table))