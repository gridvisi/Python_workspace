'''
https://www.codewars.com/kata/5b39e3772ae7545f650000fc/train/python
'''

def remove_duplicate_words(s):
    ans = []
    for i in s.split(" "):
        if i not in ans:
            ans.append(i)
    return ' '.join(ans)


#1st
def remove_duplicate_words(s):
    return ' '.join(dict.fromkeys(s.split()))

