'''
https://www.codewars.com/kata/57ee24e17b45eff6d6000164/train/python
'''

def cat_mouse(x):
    return  "Escaped!" if len(x) >= 6 else "Caught!"

#1st
def cat_mouse(x):
    return 'Escaped!' if x.count('.') > 3 else 'Caught!'