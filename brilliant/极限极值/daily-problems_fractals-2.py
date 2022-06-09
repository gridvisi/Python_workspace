'''
https://brilliant.org/daily-problems/fractals-2/

side = 2
shadow = side**2 - 0.25*side**2*pi
rate = shadow / side**2 = 1 - 0.25*pi
side *= math.sqrt(side)

s = side**2 * rate + math.sqrt(side)**2 * rate + ...
s = rate * (side**2 + math.sqrt(side)**2 +

s = rate * (4 + 2 + 1 + 1/2 + 1/4 + 1/8 ... )

if x = sum (4 + 2 + 1 + 1/2 + 1/4 + 1/8 ... )
0.5 * x = sum ( 2 + 1 + 1/2 + 1/4 + 1/8 ... )

x = 0.5*x + 4 ,so that 0.5 * x = 4, x = 8
s = rate * 8 = 8 - 2*pi
'''




