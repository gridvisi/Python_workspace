'''
https://www.codewars.com/kata/52dffa05467ee54b93000712/train/python

@test.describe('Example Tests')
def example_tests():
    test.assert_equals(pseudo_sort("I, habitan of the Alleghanies, treating of him as he is in himself in his own rights"),
     "as habitan he him himself his in in is of of own rights the treating I Alleghanies")

    test.assert_equals(pseudo_sort("take up the task eternal, and the burden and the lesson"),
    "and and burden eternal lesson take task the the the up")

    test.assert_equals(pseudo_sort("Land of the Old Thirteen! Massachusetts land! land of Vermont and Connecticut!"),
    "and land land of of the Vermont Thirteen Old Massachusetts Land Connecticut","sentence may end with a punctuation")

    test.assert_equals(pseudo_sort("Pioneers, O Pioneers!"),
    "Pioneers Pioneers O","sentence may end with a punctuation")
'''
#print(sum(['  ']))
w = 'I,'
print(w[:-1])
print('  !'[:-1].split(' '))

import string
def pseudo_sort(st):
    if not st or st.isspace():return ''
    sl = [i.strip(string.punctuation) for i in st.split(' ')]
    sl = sorted(sl,key=lambda x:x.lower())
    left = [i for i in sl if not i.istitle()]
    right = [i for i in sl if i.istitle()]
    ans = ' '.join(left + right[::-1])
    return '' if ans.isspace() else ans

st = "I, habitan of the Alleghanies, treating of him as he is in himself in his own rights"
st = 's'

st = '    !' # should equal ''
print('result:',pseudo_sort(st))

'''
    ans = ''
    sl = st.split(' ')
    for i in sl:
        if i[-1] not in string.ascii_letters:
            i = i[:-1]
    print(sl)
'''
#1st
from string import punctuation

t = str.maketrans("", "", punctuation)

def pseudo_sort(s):
    a = s.translate(t).split()
    b = sorted(x for x in a if x[0].islower())
    c = sorted((x for x in a if x[0].isupper()), reverse=True)
    return " ".join(b + c)

#2nd
def pseudo_sort(s):
    s = ''.join(i for i in s if i.isalpha() or i is ' ')
    a =  sorted(i for i in s.split() if i[0].islower())
    b =  sorted((i for i in s.split() if i[0].isupper()),key=lambda x: x.lower(),reverse=True)
    return ' '.join(a+b)

#3rd'
from re import findall

def pseudo_sort(st):
    lows = sorted(findall(r'\b[a-z]+\b', st))
    ups  = sorted(findall(r'[A-Z][A-Za-z]*', st), reverse=True)
    return ' '.join(lows + ups)