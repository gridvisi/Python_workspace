
x = ' i a m a s t ud en t '
def no_space(x):
    return ''.join(x.split(' '))

def no_space(x):
    return x.replace(' ' ,'')

print(no_space(x))

# 6 kyu Pairs of Bears
'''
'
In order to prove it's success and gain funding, the wilderness zoo needs to prove to environmentalists that it has x number of mating pairs of bears.
You must check within string (s) to find all of the mating pairs, and return a string containing only them. Line them up for inspection.
Rules: Bears are either 'B' (male) or '8' (female), Bears must be together in male/female pairs 'B8' or '8B', Mating pairs must involve two distinct bears each ('B8B' may look fun, but does not count as two pairs).
Return an array containing a string of only the mating pairs available. e.g:

'EvHB8KN8ik8BiyxfeyKBmiCMj' ---> 'B88B' (empty string if there are no pairs)

and true if the number is more than or equal to x, false if not:

(6, 'EvHB8KN8ik8BiyxfeyKBmiCMj') ---> ['B88B', false];
x will always be a positive integer, and s will never be empty

Test.assert_equals(bears(7, '8j8mBliB8gimjB8B8jlB'), ["B8B8B8",False])
Test.assert_equals(bears(3, '88Bifk8hB8BB8BBBB888chl8BhBfd'), ["8BB8B8B88B",True])
Test.assert_equals(bears(8, '8'), ["",False])
Test.assert_equals(bears(1, 'j8BmB88B88gkBBlf8hg8888lbe88'), ["8BB88B",True])
Test.assert_equals(bears(0, '8j888aam'), ["",True])
'''
n,s = 3, 'j8BmB88B88gkBBlf8hg8888lbe88'
import re
def bears(n, s):
    a = re.findall(r"B8|8B", s)
    return ["".join(a), len(a) >= n]
print(bears(n,s))

def bears(x,s):
    res,cn,ls = '',0,list(s)
    for i in range(len(s) - 1):
        if ls[i:i + 2] == ['8','B'] or ls[i:i + 2] == ['B','8']:
            res += s[i:i + 2]
            ls[i + 1] = '0'
            cn += 1
    if cn >= x: re_bool = True
    else:re_bool = False
    return [res,re_bool]