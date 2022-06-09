'''
Suppose an algorithm with an input of the list:
Apple, Banana, Carrot, Dragons.

Step 1.
If the 1st item on the list has fewer letters than the 2nd item, swap the items.

Step 2.
If the 2nd item on the list has fewer letters than the 4th item, swap the items.

Step 3.
If the 2nd item on the list has fewer letters than the 3rd item, swap the items.

Step 4. End.

What will be the list at Step 4?
'''

s = ['Apple', 'Banana', 'Carrot', 'Dragons']

def swap_s(s):
    """Judge length of items"""
    if len(s[0]) < len(s[1]):
        s[0],s[1] = s[1],s[0]

    if len(s[1]) < len(s[3]):
        s[1], s[3] = s[3], s[1]

    if len(s[1]) < len(s[2]):
        s[1],s[2] = s[2],s[1]

    return s
print(swap_s(s))
