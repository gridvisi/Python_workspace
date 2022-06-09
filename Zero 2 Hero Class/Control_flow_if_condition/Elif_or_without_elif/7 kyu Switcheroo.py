'''
https://www.codewars.com/kata/57f759bb664021a30300007d/train/python
'''
def switcheroo(string):
    ans = ''
    for i in string:
        if i == 'a':
            ans += 'b'
        elif i == 'b':
            ans += 'a'
        elif i != 'a' and i != "b":
            ans += i
    return ans

def switcheroo(s):
    return s.translate(str.maketrans('ab','ba'))

def switcheroo(string):
    #your code here
    result = ''
    for letter in string:
        if letter == 'a':
            letter = 'b'
        elif letter == 'b':
            letter = 'a'
        result += letter
    return result

def switcheroo(string):
    return ((string.replace('a','x')).replace('b','a')).replace('x','b')


def switcheroo(string):
    swap = {
        'a': 'b',
        'b': 'a',
    }
    return ''.join(swap.get(ch, ch) for ch in string)

def switcheroo(string):
    return ''.join( [ 'a' if s=='b' else 'b' if s=='a' else s for s in string ] )

switcheroo = lambda q: q.translate({97: 98, 98: 97})