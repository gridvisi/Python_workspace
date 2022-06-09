# https://www.codewars.com/kata/594adadee075005308000122/train/python



def even_and_odd(n):
    # your code here
    evn = [i for i in str(n) if not eval(i)%2]
    return list(map(int,map(''.join,[evn,[i for i in str(n) if i not in evn]])))


def even_and_odd(n):
    even, odd = '', ''
    for i in str(n):
        if eval(i) % 2:
            odd += i
        else:
            even += i

    return tuple([int(i) if len(i)>1 else 0 for i in (even,odd)])
n = 126453
n = 4628
print(even_and_odd(n))

#1st
def even_and_odd(n):
    ne = "".join(x for x in str(n) if x in "02468")
    no = "".join(y for y in str(n) if int(y) % 2)
    return tuple(0 if not a else int(a) for a in (ne, no))