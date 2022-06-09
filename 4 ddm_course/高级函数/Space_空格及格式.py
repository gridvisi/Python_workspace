'''
https://www.codewars.com/kata/5f77d62851f6bc0033616bd8/train/python

@test.describe('Sample Tests')
def sample():
    test.assert_equals(valid_spacing('Hello world'),True)
    test.assert_equals(valid_spacing(' Hello world'),False)
    test.assert_equals(valid_spacing('Hello  world '),False)
    test.assert_equals(valid_spacing('Hello'),True)
    test.assert_equals(valid_spacing('Helloworld'),True)
'''
s = 'Hello  world'
#print(s[1:],s[:-1])
def valid_spacing(s):
    if not s:return False
    if s[0] == ' ' or s[-1] == ' ':
        print('if')
        return False
    else:
        return not(any([x==y==' ' for x,y in zip(s,s[1:])]))

# any([x==y for x,y in zip(s,s[1:])])
s = 'Hello  world'
print(valid_spacing(s))


#1st solution
def valid_spacing(s):
    return s == ' '.join(s.split())
