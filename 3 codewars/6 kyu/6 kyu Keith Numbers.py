'''
https://www.codewars.com/kata/keith-numbers/solutions/python
In recreational mathematics, a Keith number or repfigit number (short for repetitive Fibonacci-like digit) is a number in the following integer sequence:
14, 19, 28, 47, 61, 75, 197, 742, 1104, 1537, 2208, 2580, 3684, 4788, 7385, 7647, 7909, ... (sequence A007629 in the OEIS)
Keith numbers were introduced by Mike Keith in 1987. They are computationally very challenging to find, with only about 100 known.
Implement the code to check if the given number is a Keith number. Return the number number of iteration needed to confirm it; otherwise return false.
Note: 1-digit numbers are not Keith numbers by definition
Examples
n = 197      # --> [1, 9, 7]
# calculation           iteration
1 + 9 + 7 = 17         #    1
9 + 7 + 17 = 33        #    2
7 + 17 + 33 = 57       #    3
17 + 33 + 57 = 107     #    4
33 + 57 + 107 = 197    #    5

[14, 19, 28, 47, 61, 75, 197, 742, 1104, 1537, 2208, 2580, 3684, 4788, 7385, 7647, 7909, 31331, 34285, 34348, 55604,
62662, 86935, 93993]
'''

def is_keith_number(n):
    numList = [int(i) for i in str(n)]  # int array
    if len(numList) > 1:  # min 2 digits
        itr = 0
        while numList[0] <= n:
            # replace array entries by its sum:
            numList[itr % len(numList)] = sum(numList)
            itr += 1
            if n in numList:  # keith-condition
                return itr
    return False

print(is_keith_number(197))
res = []
for n in range(1,100000):
    #res = []  why not type collection define here?
    if is_keith_number(n) != False:
        res.append(n)
print(res)

def is_keith_number(n):
    if n <= 10: return False
    c, k_lst, k_num = 0, list(str(n)), n
    while k_num <= n:
        k_num = sum([int(x) for x in k_lst])
        c += 1
        if k_num == n: return c
        k_lst.append(k_num)
        k_lst.pop(0)
    return False

def is_keith_number(n):
    def rec(ds, i):
        d = sum(ds)
        ds = ds[1:]
        ds.append(d);
        return i if d == n else False if d > n else rec(ds, i + 1)
    return False if n < 10 else rec([int(x) for x in list(str(n))], 1)

# It's nice to put the OEIS but it's not that interesting if they give the algo
def is_keith_number(n):
    if n < 10: return False
    x = list(map(int, str(n)))
    y, i = sum(x), 1
    while y < n:
        i, x, y = i+1, x[1:]+[y], 2*y-x[0]
    return i * (y==n)

def is_keith_number(n):
    res = [int(x) for x in str(n)]
    tmp = sum(res)
    cnt = 1
    while tmp < n:
        cnt += 1
        res.pop(0)
        res.append(tmp)
        tmp = sum(res)
        if tmp == n:
            return cnt
    return False

from itertools import count

def is_keith_number(n):
    lst = list(map(int,str(n)))
    s   = sum(lst)
    for i in count(1):
        if s>=n: return n>9 and s==n and i
        lst, s = lst[1:] + [s], s*2-lst[0]

def is_keith_number(n):
    store,li,s = [int(i) for i in str(n)],[],0
    while s < int(n) and s != n:
        s = sum(store) ; store = store[1:] + [s] ; li.append(s)
    return len(li) if len(str(n)) > 1 and li and li[-1] == n else False

def is_keith_number(n):
    interactions = 1
    input_list = [int(x) for x in str(n)]

    while sum(input_list) < n:
        input_list.append(sum(input_list))
        del input_list[0]
        interactions+=1

    return interactions if len(input_list)>1 and sum(input_list)==n else False