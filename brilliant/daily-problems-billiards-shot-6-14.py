
'''
0  1
 \/
 /\
2  3
'''
# Some necessary system libraries
import sys

# import numpy as np

# Define billiard table style
'''
0  : nothing
1  : left edge
2  : upper edge
-1 : right edge
-2 : bottom edge
3  : top left bag
4  : right top bag
5  : left bottom bag
6  : right bottom bag
Note that 0,1,2,3 here do not refer to directions!
'''
'''
Update 2020.8.19 00:03(Beijing time)
Billiard tables are not easy to create manually.
Here is a python function to generate a billiard table.
It can do without the Numpy library.
Thanks to Chris Russell for his suggestion!

[[3]+[2 for x in range(0,a-2)]+[4]] generates the first row
[[1]+[0 for y in range(0,a-2)]+[-1] for x in range(0,b-2)] generate the second line to the penultimate line
[[5]+[-2 for x in range(0,a-2)]+[6]] generates the last row

These two lines of code can replace the big one below
'''
def f(b ,a):
    return [[3]+[2 for x in range(0 , a-2)] +[4]]+[[1] +[0 for y in range(0, a-2)]+[-1] for x in range(0, b-2)]+[[5] +[-2 for x in range(0, a-2)]+[6]]
table =f(6 ,14  )# The length and width of the billiard table are 6 and 14 respectively
'''
This is the original code:
table=np.array([
[3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1],
[5,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2, 6]])
'''
# Record the route that has been taken
repeat =[0 for x in range(0 ,50000)]

# Offset in each direction
# For example, when the direction is 2
# dx[2] is 1, which means that the x coordinate needs to be increased by 1 for the next move
# dy[2] is -1, which means that the y coordinate needs to be increased by -1 for the next move
dx =[-1 ,-1 ,1 ,1]
dy =[-1 ,1 ,-1 ,1]

# Initialization
# At the beginning, the direction of the ball is 3 and the coordinates are (1,1) x= 1
x = 1
y = 1
way = 3

# Ball bag corresponding to each number
# In the multi-line comment above, 3 represents the top left bag, so the third position of this array is the 'top left'. The other is the same
ans = ['', '', '', 'top left', 'top right', 'bottom left', 'bottom right']

while table[x][y] <= 2:
    if repeat[way * 10000 + x * 100 + y] == 1:  # If the previous situation is repeated
        print('It bounces around forever.')  # Don’t fantasize about getting into the bag!
        sys.exit(0)  # Exit the program
    repeat[way * 10000 + x * 100 + y] = 1  # Record the current situation
    x = x + dx[way]  # Calculate new x values
    y = y + dy[way]  # Calculate new y values
    if table[x][y] != 0:  # If it hits the edge
        way = way + table[x][y]  # Calculate the new direction
print('It falls in the', ans[table[x][y]], 'pocket.')  # Print answer
