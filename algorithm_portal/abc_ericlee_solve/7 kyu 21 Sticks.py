
'''

https://www.codewars.com/kata/5866a58b9cbc02c4f8000cac/train/python

21 sticks in the pile

Bob takes 2  -->  19 sticks left
Jim takes 3  -->  16 sticks
Bob takes 3  -->  13 sticks
Jim takes 1  -->  12 sticks
Bob takes 2  -->  10 sticks
Jim takes 2  -->   8 sticks
Bob takes 3  -->   5 sticks
Jim takes 3  -->   2 sticks
Bob takes 2  -->  Bob wins!
'''
# we judge the match point in advance by
#win = sticks so that lose = stick -4
#win = sticks -5, lose = stick - 5 -4

def makeMove(sticks):
    win = sticks
    while win > 0:
        win -= 4
        ans = win
    return ans + 5
sticks = 21
print(makeMove(sticks))

# 1st solution
def makeMove(sticks):
    return max(sticks % 4, 1)