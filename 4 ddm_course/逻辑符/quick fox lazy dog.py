'''
'the quick brown fox jumped over the lazy dog'
all(iterable, /)
    Return True if bool(x) is True for all values x in the iterable.如果所有的值都为True，则返回True。
    
char = 'the quick brown fox jumped over the lazy dog'
char = 'the quick brown fox jumps over a lazy dog'
alpha = 'abcdefghijklmnopqrstuvwxyz '
'''

def char_in_alpha(char,alpha):
    it = iter(char.lower())
    print(it)
    return all(c in it for c in alpha.lower())

print([i%2==0 for i in range(10)])
print([i for i in range(10) if i%2 == 0])
print('all use : ',all(x%2 == 0 for x in [i for i in range(10) if i%2==0]))


def char_in_alpha(char,alpha):
    re = ''
    for c in alpha.lower():
        if c in char.lower():
            pass
            #return re
        else:re += c
    return re

char = 'Albert Einstein'
alpha ="If All the bees die on earth, we would die due to not enough food sustain the living"

char = 'the quick brown fox jumped over the lazy dog'
char = 'the quick brown fox jumps over a lazy dog'
char = 'abcdefghijklmnopqrstuvw '
alpha = 'abcdefghijklmnopqrstuvwxyz '
print(char_in_alpha(char,alpha))