# https://brilliant.org/daily-problems/taxicab-distance-2/
'''
In New Math City (NMC), streets follow a square grid with integer
coordinates, and all distances are measured in terms of vertical
and horizontal units along these streets.

Obi wants to live at exactly the same distance from both his work
located at (4,-2)(4,−2) and the favorite pub at (-3, 2).(−3,2).

How many potential grid points with integer coordinates can he
consider?
'''

point = [(0,-0.875),(0.5,0)]
#suppose: y = a*x + b :
# 0.5*a + b = 0  and -0.875 = 0*a + b
# b = -0.875, a = 0.875/0.5 = 1.75
# y = 1.75 * x - 0.875

ans,cunt = [],0
for x in range(-100,100,1):
    y = 1.75 * x - 0.875
    if int(y) == y:
        ans.append((x,y))
        cunt += 1
print(ans,cunt)
