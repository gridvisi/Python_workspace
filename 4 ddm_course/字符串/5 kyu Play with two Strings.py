'''
https://www.codewars.com/kata/56c30ad8585d9ab99b000c54/train/python

Input: "abc" and "cde"      => Output: "abCCde"
Input: "ab" and "aba"       => Output: "aBABA"
Input: "abab" and "bababa"  => Output: "ABABbababa"
'''
a, b = "ABAB", "bababa"
print(a.count('a'),a.lower())
a,b = "abc" , "cde"
a,b = "abcdeFg", "defgG"  #"abcDEfgDEFGg"

def work_on_strings(a,b):
    left = [i if b.lower().count(i.lower())%2 == 0 else i.swapcase() for i in a]
    right = [i if a.lower().count(i.lower())%2 == 0 else i.swapcase() for i in b]
    return ''.join(left)+''.join(right)       #,left.append(right)

print(work_on_strings(a,b))

def work_on_strings(a, b):
    new_a = [letter if b.lower().count(letter.lower()) % 2 == 0 else letter.swapcase() for letter in a]
    new_b = [letter if a.lower().count(letter.lower()) % 2 == 0 else letter.swapcase() for letter in b]
    return ''.join(new_a) + ''.join(new_b)