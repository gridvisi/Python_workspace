'''
https://www.codewars.com/kata/60d20fe1820f1b004188ceed/train/python
Task
Given three sides a, b and c, determine if a triangle can
be built out of them.

Code limit
Your code can be up to 40 characters long.

Note
Degenerate triangles are not valid in this kata.

PUZZLESGAMES
'''
def triangle(a, b, c):
    t = [a,b,c]
    return sum(t) - max(t) > max(t)

#1st
triangle=lambda*a:2*max(a)<sum(a)