# https://www.codewars.com/kata/5888cba35194f7f5a800008b/train/python
'''
@test.describe('Example Tests')
def example_tests():
    test.assert_equals(asterisc_it(5312708), '531270*8')
    test.assert_equals(asterisc_it(9682135), '96*8*2135')
    test.assert_equals(asterisc_it(2222), '2*2*2*2')
    test.assert_equals(asterisc_it(1111), '1111')
    test.assert_equals(asterisc_it(9999), '9999')
    test.assert_equals(asterisc_it('0000'), '0*0*0*0')
    test.assert_equals(asterisc_it(8), '8')
    test.assert_equals(asterisc_it(2), '2')
    test.assert_equals(asterisc_it(0), '0')
    test.assert_equals(asterisc_it([1, 4, 64, 68, 67, 23, 1]), '14*6*4*6*8*67231')

from queue import queue
from queue import deque
'''
n = 5312708
n = [1, 4, 64, 68, 67, 23, 1]
print(isinstance(n[0],int))
print(isinstance(str(n)[0],str))
#print(isinstance(n,list))
#print(''.join([str(i) for i in str(n)]))

def asterisc_it(n):
    re,i = [],0
    if isinstance(n,int):n = str(n)
    n = ''.join([str(i) for i in n])
    print(n)
    re = ['*'+n[i+1] if int(n[i])%2==0 and int(n[i+1])%2==0 else n[i+1] for i in range(len(n)-1)]
    return n[0]+''.join(re)
print(asterisc_it(n))

import re

def asterisc_it(s):
    if   isinstance(s,int):  s=str(s)
    elif isinstance(s,list): s=''.join(map(str,s))
    return re.sub(r'(?<=[02468])(?=[02468])', '*', s)
'''
def asterisc_it(n):
    re = []
    if isinstance(n,int):
        n = str(n)
    elif isinstance(n,list):
        n = list(''.join(n))
        print(n)
    for i in range(len(n)-1):
        if int(n[i])%2 == 0 and int(n[i+1])%2 == 0:
            re.append(f'{n[i]}'+'*'+ f'{n[i+1]}')
        else:re.append(n[i])
    return re
print(asterisc_it(n))
'''

'''
import queue
from collections import deque
def asterisc_it(n):
    re,ls = '',str(n)
    q = deque(str(n))
    #print(q.popleft())
    for i in range(len(q)):
        #print(q)
        if int(ls[i]) % 2 == 0:
            re += q.popleft()
            print(q)
            if int(ls[i]) % 2 == 0:
                re += '*'+q.popleft()
        else:re += q.popleft()
    return re
print(asterisc_it(n))


'''


