'''
test.describe("Find the missed number")
test.it("should pass basic test case")

# Basic test

string = "1116122137143151617181920849510"
test.assert_equals(find_number(1, 21, string), [12, 21])

test.describe("Find the missed number")
test.it("should pass basic test case")

# Basic test

string = "1116122137143151617181920849510"
test.assert_equals(find_number(1, 21, string), [12, 21])
'''
# 1st solution
from collections import Counter
from itertools import permutations

def find_number(start, stop, s):
    miss = Counter(''.join(map(str, range(start, stop+1)))) - Counter(s)
    print([c*n for c,n in Counter(s).items()])
    print(''.join(c * n for c, n in Counter(s).items()))
    print(''.join(c*n for c,n in miss.items()))
    print(miss,Counter(s),Counter(''.join(map(str, range(start, stop+1)))))
    intValues = {int(v) for v in map(''.join, permutations(''.join(c*n for c,n in miss.items()))) if v and v[0] != '0'}
    return [v for v in intValues if start <= v <= stop ]
start, stop, string = 1,21, "2198765123416171890101112131415"
print(find_number(start, stop, string))

#Top 2nd
from collections import Counter

def find_number(start, stop, string):
    missing_digits = Counter("".join(str(n) for n in range(start, stop + 1))) - Counter(string)
    return [n for n in range(start, stop + 1) if Counter(str(n)) == missing_digits]



def find_number(start, stop, string):
    res = []
    bench = sum([sum([int(j) for j in str(i)]) for i in range(start,stop+1)]) - sum([int(i) for i in string])
    gap = len(''.join([str(i) for i in range(start,stop+1)])) - len(string)
    for num in range(start, stop + 1):
        if sum([int(i) for i in str(num) if len(str(num)) == gap]) == bench:
            if string.find(str(num-1)) != -1 and string.find(str(num+1)) != -1:
                res.append(num)
    return res,gap

start, stop, string = 1,21, "1116122137143151617181920849510"
start, stop, string = 5,10,"578910"
start, stop, string = 1,21, "2198765123416171890101112131415"
print('in:',string.find('12'))
print('in:',string.find('150'))
print(find_number(start, stop, string))

def find_number(start, stop, string):
    bench = [str(i) for i in range(start, stop + 1)]
    print(bench)
    i, j,re = 0,1,[]
    while j <= len(string)+1:
        if string[i:j] not in re:
            re.append(string[i:j])
            i = j
            j += 1
        else:
            j += 1
    #if j == len(string):
    return [i for i in bench if i not in re],re
start, stop, string = 1,21, "1116122137143151617181920849510"
#start, stop, string = 5,10,"578910"
start, stop, string = 1,21, "2198765123416171890101112131415"
print(find_number(start, stop, string))
bench = ''.join([str(i) for i in range(start, stop + 1)])

print(len(bench),len(string))

import difflib
d = difflib.Differ()
diff = d.compare(bench, string)
#print(''.join(diff))



def find_number(start, stop, string):

    #bench = ''.join([str(i) for i in range(start, stop + 1)])
    bench = [str(i) for i in range(start, stop + 1)]
    re = bench
    print(string,bench)
    for x in bench:
        #print(x)
        if x in string:
            #bench = bench.replace(x,'')
            bench.remove(x)
            print(x,bench)
    return bench
start, stop, string = 5,10,"578910"
start, stop, string = 1,21, "1116122137143151617181920849510"
start, stop, string = 1,21, "2198765123416171890101112131415"
#print(find_number(start, stop, string))

'''
x = '6'
string = '812364'
if x in string:
    print(string.replace(x,''))
print(int('13'))

'''

import difflib

#if__name__ == '__main__':
text1 = """Python is 30 years old.
    Many people love it.
    You should learn it now."""
text1_lines = text1.splitlines()

text2 = """Python is 31 years old.
    Many people loves it.
    We all should learn it now.
    Just do it."""
text2_lines = text2.splitlines()

d = difflib.Differ()
diff = d.compare(text1_lines, text2_lines)
print('\n'.join(diff))