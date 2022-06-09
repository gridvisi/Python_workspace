'''
https://www.codewars.com/kata/5650ab06d11d675371000003/train/python
'''

def split_in_parts(s, part_length):
    # your code here
    return ' '.join([s[i:i+part_length] for i in range(len(s))[::part_length]])
s,part_length = "supercalifragilisticexpialidocious", 3
print(split_in_parts(s,part_length))


#1st
from textwrap import wrap
def split_in_parts(s, part_length):
    return " ".join(wrap(s,part_length))