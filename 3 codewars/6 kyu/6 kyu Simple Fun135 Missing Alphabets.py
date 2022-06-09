'''
https://www.codewars.com/kata/58a664bb586e986c940001d5/train/python
Test.it("Basic Tests")
Test.assert_equals(missing_alphabets("abcdefghijklmnopqrstuvwxy"),"z")
Test.assert_equals(missing_alphabets("abcdefghijklmnopqrstuvwxyz"),"")
Test.assert_equals(missing_alphabets("aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyy"),"zz")
Test.assert_equals(missing_alphabets("abbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxy"),"ayzz")
Test.assert_equals(missing_alphabets("codewars"),"bfghijklmnpqtuvxyz")

'''
print(2*'miss')
test = ['a','b','a']
test.remove('a')
print(test)


from collections import Counter
from string import ascii_lowercase
def missing_alphabets(s):
    c = Counter(s)
    m = max(c.values())
    return ''.join(letter * (m - c[letter]) for letter in ascii_lowercase)

s = "abbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxy"
s = "codewars"
s = "abcdefghijklmnopqrstuvwxyz"
s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyy"
print(missing_alphabets(s))


from collections import Counter
from string import ascii_lowercase as alphabet

def missing_alphabets(s):
    counts = Counter(s)
    max_count = max(counts.values())
    return ''.join(c * (max_count - counts[c]) for c in alphabet)
'''

import string
from collections import Counter
def missing_alphabets(s):
    alphdict = Counter(s)
    return [k for k,v in alphdict.items() if v != max(alphdict.values())]
s = "abbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxy"
print(missing_alphabets(s))
'''

'''
import string
def missing_alphabets(s):
    return ''.join([i.lower() for i in string.ascii_letters[:26] if i not in s])
s = "codewars"
print(missing_alphabets(s))
Test Passed
Test Passed
'z' should equal 'zz'
'z' should equal 'ayzz'
Test Passed
'''


