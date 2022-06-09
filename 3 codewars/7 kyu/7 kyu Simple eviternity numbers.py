'''
https://www.codewars.com/kata/5b93f268563417c7ed0001bd/train/python

Test.it("Basic tests")
Test.assert_equals(solve(0,100),4)
Test.assert_equals(solve(0,1000),14)
Test.assert_equals(solve(0,10000),37)
Test.assert_equals(solve(0,100000),103)
Test.assert_equals(solve(0,500000),148)
'''
print(['5', '8'] in ['3','5','8'])


from collections import Counter
a,b = 0,500000
print(Counter(list(str(585))))
print(sorted(Counter(list(str(585)))))
print(set(Counter(list(str(585)))))

def solve(a,b):
    ans,cunt = [],0
    for n in range(a, b + 1):
        if set(Counter(list(str(n)))).issubset(['3', '5', '8']):
            if Counter(list(str(n)))['8'] >= Counter(list(str(n)))['5'] >= Counter(list(str(n)))['3']:
                cunt += 1
    return cunt
    #return len(ans)
#print(solve(a,b))

def solve(a,b):
    ans = []
    #fit = [n for n in range(a,b+1) if set(list(str(n))).issubset(['3','5','8'])]
    fit = [Counter(list(str(n))) for n in range(a, b + 1) if set(Counter(list(str(n)))).issubset(['3','5','8'])]
    #print(fit)
    for d in fit:
        if d['8'] >= d['5'] >= d['3']:
            ans.append(d)
    return len(ans)

#1st solution
u = [8, 58, 85, 88, 358, 385, 538, 583, 588, 835, 853, 858, 885, 888, 3588,
     3858, 3885, 5388, 5588, 5838, 5858, 5883, 5885, 5888, 8358, 8385, 8538,
     8558, 8583, 8585, 8588, 8835, 8853, 8855, 8858, 8885, 8888, 35588, 35858,
     35885, 35888, 38558, 38585, 38588, 38855, 38858, 38885, 53588, 53858, 53885,
     53888, 55388, 55838, 55883, 55888, 58358, 58385, 58388, 58538, 58583, 58588,
     58835, 58838, 58853, 58858, 58883, 58885, 58888, 83558, 83585, 83588, 83855,
     83858, 83885, 85358, 85385, 85388, 85538, 85583, 85588, 85835, 85838, 85853,
     85858, 85883, 85885, 85888, 88355, 88358, 88385, 88535, 88538, 88553, 88558,
     88583, 88585, 88588, 88835, 88853, 88855, 88858, 88885, 88888, 335588, 335858,
     335885, 338558, 338585, 338855, 353588, 353858, 353885, 355388, 355838, 355883,
     355888, 358358, 358385, 358538, 358583, 358588, 358835, 358853, 358858, 358885,
     358888, 383558, 383585, 383855, 385358, 385385, 385538, 385583, 385588, 385835,
     385853, 385858, 385885, 385888, 388355, 388535, 388553, 388558, 388585, 388588,
     388855, 388858, 388885]

def solve(a, b):
    return sum(a <= x < b for x in u)

#2nd solution
from collections import Counter
from itertools import product
def valid(s):
    s = str(s)
    c = Counter(s)
    print(c)
    return c[8] >= c[5] >= c[3]
s = 1000
print('The 2nd solution:',valid(s))

def ever(n):
    s = str(n)
    C = [s.count('3'), s.count('5'), s.count('8')]
    if sum(C)==len(s) and sorted(C)==C :
        return True
    return False

D={i for i in range(1000000) if ever(i)}
def solve(a,b):
    return len({e for e in D if e>=a and e<=b})
a,b = 1,500000
print('The 2nd solution:',solve(a,b))


#3rd solution
ALL = [int(''.join(map(str, digs))) for nd in range(1, 7)
       for digs in product((3, 5, 8), repeat=nd)
       if valid(digs)]

def solve(a, b):
    return sum(a <= n < b for n in ALL)

#3-1 solution
eviternity = [int(n) for n in map(str, range(10 ** 6))
              if set(n) <= set('358') and n.count('3') <= n.count('5') <= n.count('8')]
solve = lambda a, b, f=__import__('bisect').bisect_left: f(eviternity, b) - f(eviternity, a)



#4th solution
import itertools

def merge(l):
    return ''.join(l)

def solve(a,b):
    digits=['3', '5', '8','']
    c2=set(map(merge,itertools.product(digits,digits,digits,digits,digits,digits)))
    c2.remove('')
    c=0
    for n in c2:
        if int(n)>=a and int(n)<b:
               if n.count('8')>= n.count('5') and n.count('5')>= n.count('3'):
                    c+=1
    return c


#5th solution
from itertools import product
def solve(a,b):
    res, start, stop = [], len(str(a)), len(str(b))+1
    for i in range(start, stop):
        res += ["".join(x) for x in product('538', repeat=i)]
    return sum(1 for x in res if a<=int(x)<=b and x.count('8')>=x.count('5')>=x.count('3'))

#6th solution
def solve(a,b):
    count = 0
    for i in map(str, range(a, b)):
        for j in i:
            if j not in '853':
                break
        else:
            if i.count('8') >= i.count('5') >= i.count('3'): count += 1
    return count


#7th solution
from re import match
memo = {}
def solve(a, b):
    return sum(1 for n in range(a, b) if is_eviternity(n))

def is_eviternity(n):
    if n not in memo:
        s = str(n)
        memo[n] = match(r'[853]+$', s) and s.count('8') >= s.count('5') >= s.count('3')
    return memo[n]


'''

def solve(a,b):
    ans = []
    for n in range(a,b+1):
        if '8' and '5' and '3' and '0' in str(n):

            ans.append(n)
    return len(ans)
    
            if '5' not in str(n):
                
            
'''

#8th solution
from collections import Counter
from bisect import bisect

evi = []
snums = set("1246790")
for i in map(str, range(500000)):
    s = set(i)
    if s - snums == s and "8" in s:
        c = Counter(i)
        if c.get("3",0) <= c.get("5",0) <= c.get("8",0):  evi+=int(i),
def solve(a,b):
    return bisect(evi,b) - bisect(evi,a-1)

#9th solution
from functools import lru_cache

@lru_cache(maxsize=None)
def f_checker(num):
    if all([i in ['3', '5', '8'] for i in str(num)]):
            count_8 = str(num).count('8')
            count_5 = str(num).count('5')
            count_3 = str(num).count('3')
            if count_8 >= count_5 and count_5 >= count_3:
                return num
def solve(a,b):
    counter = 0
    for num in range(a, b):
        res = f_checker(num)
        if res:
            counter += 1
    return counter

#10 solution
from itertools import product
from typing import List, Iterator

def generate_numbers(max_number) -> Iterator[int]:
    def gen(current, count8, count5, count3) -> Iterator[int]:
        if current > max_number:
            return
        if count8 >= count5 and count5 >= count3 and current > 0:
            yield current
        yield from gen(current*10+3, count8, count5, count3+1)
        yield from gen(current*10+5, count8, count5+1, count3)
        yield from gen(current*10+8, count8+1, count5, count3)
    return gen(current=0, count8=0, count5=0, count3=0)

def solve(a: int, b: int) -> int:
    numbers = filter(lambda n: n >= a, generate_numbers(b))
    return len(list(numbers))

#11 solution
from collections import Counter


def test_evit(num):
    if any(x in str(num) for x in '0124679'):
        return False
    c = Counter(str(num))
    return c['8'] >= c['5'] >= c['3']


d = {}

def solve(a, b):
    c = 0

    for i in range(a, b):
        if i in d.keys():
            c += d[i]
        else:
            t = test_evit(i)
            c += t
            d[i] = t

    return c

#12th solution
from itertools import product
def solve(a,b):
    res, start, stop = [], len(str(a)), len(str(b))+1
    for i in range(start, stop):
        res += ["".join(x) for x in product('538', repeat=i)]
    return sum(1 for x in res if a<=int(x)<=b and x.count('8')>=x.count('5')>=x.count('3'))

#13th solution
from bisect import bisect_left

Memo = [8, 58, 85, 88, 358, 385, 538, 583, 588, 835, 853, 858, 885, 888]
for i in range(889, 388885+1):
    s = str(i)
    if all([d in '853' for d in s]):
        e = s.count('8')
        f = s.count('5')
        t = s.count('3')
        if e >= f and f >= t:
            Memo.append(i)

def solve(a, b):
    return bisect_left(Memo, b) - bisect_left(Memo, a)