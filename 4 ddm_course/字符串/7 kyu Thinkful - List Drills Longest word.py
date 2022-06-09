'''
https://www.codewars.com/kata/58670300f04e7449290000e5/train/python
'''

def longest(words):
    return max(list(map(len,word)))
word = ['explicit', 'is', 'better', 'than', 'implicit']
print(longest(word))

#1st solution
def longest(words):
    return max(map(len, words))