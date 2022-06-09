'''
https://www.codewars.com/kata/56e9e4f516bcaa8d4f001763/train/python

Test Results:
 Example Tests
21 should equal '0+1+2+3+4+5+6 = 21'
28 should equal '0+1+2+3+4+5+6+7 = 28'
-1 should equal '0=0'
-1 should equal '-1<0'
-1 should equal '-10<0'
'''

def show_sequence(n):
    out = '+'.join([str(i) for i in range(n+1)])
    return f"{out} = " + str(sum([i for i in range(n+1)])) if n >= 0 else f"{n} < 0"
n = -1
print(show_sequence(n))

def show_sequence(n):
    if n == 0:
        return "0=0"
    elif n < 0:
        return str(n) + "<0"
    else:
        counter = sum(range(n+1))
        return '+'.join(map(str, range(n+1))) + " = " + str(counter)

def show_sequence(n):
    if n < 0:
        return '%s<0' % n
    elif n == 0:
        return '0=0'
    numbers = range(n+1)
    return '%s = %s' % ('+'.join(map(str, numbers)), sum(numbers))