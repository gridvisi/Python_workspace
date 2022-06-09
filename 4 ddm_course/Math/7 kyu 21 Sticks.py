'''
https://www.codewars.com/kata/5866a58b9cbc02c4f8000cac/solutions
'''

def makeMove(sticks):
    return max(sticks % 4, 1)