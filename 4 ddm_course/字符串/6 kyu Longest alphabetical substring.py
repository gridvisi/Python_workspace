'''
https://www.codewars.com/kata/5a7f58c00025e917f30000f1/train/python
Test.assert_equals(longest('asd'), 'as')
Test.assert_equals(longest('nab'), 'ab')
Test.assert_equals(longest('abcdeapbcdef'), 'abcde')
Test.assert_equals(longest('asdfaaaabbbbcttavvfffffdf'), 'aaaabbbbctt')
Test.assert_equals(longest('asdfbyfgiklag'), 'fgikl')
Test.assert_equals(longest('z'), 'z')
Test.assert_equals(longest('zyba'), 'z')
'''
print(ord('a'))
st = ['aaaabbbbcttdff','as', 'as', 'df', 'aa', 'aa', 'ab', 'bb', 'bb', 'bb', 'bc', 'ct', 'tt', 'aaaabbbbctt']
#print(sorted(st,key=lambda x:len(x) and ord(x[0])))
st.sort(key=lambda x:len(x),reverse=True)
#print(st[0])

def longest(s):
    if len(s) == 1:return s
    i, j, re,res = 0, 1,'',[]
    while j <= len(s):
        if list(s[i:j]) == sorted(list(s[i:j])):
            print('cmp:',s[i:j],sorted(list(s[i:j])))
            if len(s[i:j]) > len(re):
                re = s[i:j]
            j += 1
        else:
            i = j-1
            j += 1
            print(s,re,i,j)
    return re

#max(re,key=lambda x:len(x))
#sorted(res,key=lambda x:len(x) or ord(x[0]),reverse=True)[0],res
#s = 'asdfaaaabbbbcttavvfffffdf' #'aaaabbbbctt'
#s = 'asdfbyfgiklag' #'fgikl'
s = 'nab'
#s = 'zyba'
#s = 'abcdeapbcdef'
#s = 'z'

# 1st solution
import re
reg = re.compile('a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*')
def longest(s):
    return max(reg.findall(s), key=len)
print(longest(s))

#3rd solution
def longest(string):
    start = 0
    longest = string[0:1]
    length = len(string)
    for i in range(1, length):
        if string[i] < string[i - 1] or i == length - 1:
            if string[i] < string[i - 1]:
                last = string[start:i]
                start = i
            else:
                last = string[start:]
            if len(last) > len(longest):
                longest = last
    return longest

# 4th solution
import re
def longest(s):
    return max(re.findall(r'a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*',s),key=len)

# 5th solution
def longest(s):
    k = []
    for i in range(len(s)-1):
        if s[i] <= s[i+1]:
            k.append(s[i])
        else:
            k.append(s[i])
            k.append(' ')
    k += s[-1]
    return max(''.join(k).split(), key=len)

# 6th solution
def longest(s):
    chunks = []
    for c in s:
        if chunks and chunks[-1][-1] <= c:
            chunks[-1] += c
        else:
            chunks.append(c)
    return max(chunks, key=len)

#7th solution
def longest(s):
    max_substring = ""
    substring = ""
    for ch in s:
        if substring == "" or ord(ch) >= ord(substring[-1]):
            substring += ch
        elif ord(ch) < ord(substring[-1]):
            substring = "".join(ch)
        if len(substring) > len(max_substring):
            max_substring = substring
    return max_substring

# 8th solution
import re
def longest(s):
    myreg = 'a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*'
    return max(re.findall(r'(' + myreg + ')', s), key=len)


'''
def longest(s):
    if len(s) == 1:return s
    i, j, res = 0, 1, []
    while j < len(s):
        if ord(s[j]) >= ord(s[i]):
            res.append(s[i:j+1])
            i += 1
            j += 1
        else:
            res.append(s[:i+1])           

            s = s[j:]
    return max(res,key=lambda x:len(x))
'''