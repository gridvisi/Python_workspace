'''
https://brilliant.org/daily-problems/os-make-15/

1  2  3 = 15
3  2  1 = 15
'''

from itertools import product
ops = ["+", "-", "/", "*", ""] #concatenation is an empty sting!

for a,b in product(ops, repeat=2):
  if eval("1" + a + "2" + b + "3") == 15:
      print(a,',',b)
      print("A")
  if eval("3" + a + "2" + b + "1") == 15:
      print(a,b)
      print("B")