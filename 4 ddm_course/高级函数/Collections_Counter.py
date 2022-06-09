from collections import Counter
s = [3,3,3,5,5,7,7,2,9]
print(Counter(s))

str = "THE QUICK BROWN FOX JUMPS OVER A LAZY DOG"
print(Counter(str))
print(sorted(Counter(str)))
import string
print(string.ascii_uppercase)
print(string.ascii_uppercase in ''.join(sorted(Counter(str))))

str_dict = Counter(str)
rep = [(k,v) for k,v in str_dict.items() if str_dict[k] > 1]
print(rep)
repeat = ['O','E','U','R','A']

# [('E', 2), (' ', 8), ('U', 2), ('R', 2), ('O', 4), ('A', 2)]
s_update = 'EURO EURO OOAA'
print('update:',Counter(str) - Counter(s_update))