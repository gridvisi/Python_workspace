'''
https://www.codewars.com/kata/53697be005f803751e0015aa/train/python
a -> 1
e -> 2
i -> 3
o -> 4
u -> 5
test.assert_equals(encode('hello'), 'h2ll4')
test.assert_equals(encode('How are you today?'), 'H4w 1r2 y45 t4d1y?')
test.assert_equals(encode('This is an encoding test.'), 'Th3s 3s 1n 2nc4d3ng t2st.')
test.assert_equals(decode('h2ll4'), 'hello')
'''


def encode(st):
    code = dict(zip("aeiou",'12345'))
    return ''.join([code[i] if i in code else i for i in st])

print(encode())


def decode(st):
    code = dict(zip('12345',"aeiou"))
    return ''.join([code[i] if i in code else i for i in st])

#1st solution
def encode(s, t=str.maketrans("aeiou", "12345")):
    return s.translate(t)

def decode(s, t=str.maketrans("12345", "aeiou")):
    return s.translate(t)

#2nd solution
CIPHER = ("aeiou", "12345")


def encode(st):
    return st.translate(str.maketrans(CIPHER[0], CIPHER[1]))

def decode(st):
    return st.translate(str.maketrans(CIPHER[1], CIPHER[0]))