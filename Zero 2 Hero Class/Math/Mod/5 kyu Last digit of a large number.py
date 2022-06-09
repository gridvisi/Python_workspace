'''
https://www.codewars.com/kata/5511b2f550906349a70004e1/train/python
last_digit(4, 1)                # returns 4
last_digit(4, 2)                # returns 6
last_digit(9, 7)                # returns 9
last_digit(10, 10 ** 10)        # returns 0
last_digit(2 ** 200, 2 ** 300)  # returns 6
'''

def digitloop():
    last = {}
    for x in range(10):
        #last = dict() #last[x] = []是个坑
        i,value = x,[]
        while int(str(i)[-1]) not in value:
            value.append(int(str(i)[-1]))
            i *= x
        last[x] = value
    return last

    #return last
print(digitloop())


def last_digit(n1, n2):
    l = int(str(n1)[-1])
    return digitloop()[l][n2 % len(digitloop()[l]) - 1]


#1st
def last_digit(n1, n2):
    return pow(n1, n2, 10)

#2nd
rules = {
    0: [0,0,0,0],
    1: [1,1,1,1],
    2: [2,4,8,6],
    3: [3,9,7,1],
    4: [4,6,4,6],
    5: [5,5,5,5],
    6: [6,6,6,6],
    7: [7,9,3,1],
    8: [8,4,2,6],
    9: [9,1,9,1],
}
def last_digit(n1, n2):
    ruler = rules[int(str(n1)[-1])]
    return 1 if n2 == 0 else ruler[(n2 % 4) - 1]

#3rd
def last_digit(n1, n2):
    return (n1 % 10) ** (n2 % 4 + 4 * bool(n2)) % 10


#4th
def last_digit(n1, n2):
    last_dict = {
        0: [0],
        1: [1],
        2: [2, 4, 6, 8],
        3: [3, 9, 7, 1],
        4: [4, 6],
        5: [5],
        6: [6],
        7: [7, 9, 3, 1],
        8: [8, 4, 2, 6],
        9: [9, 1]}

    if n2 == 0:
        return 1
    a = n1 % 10
    return last_dict[a][(n2 - 1) % len(last_dict[a])]

#5th
def last_digit(b, e):
  res, b = 1, b % 10
  while e > 0:
    if e & 1: res = res * b % 10
    e >>= 1
    b = b * b % 10
  return res % 10


#6
def last_digit(n1, n2):
    return (n1 % 10) ** min(n2 % 4 or 4, n2) % 10

