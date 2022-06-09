# https://brilliant.org/daily-problems/lune-area-3/

import math
r = math.sqrt(21*21 + 34*34) * 0.5
semicircle = math.pi*((34/2)**2 + (21/2)**2)
circle = math.pi * r**2
shaded = semicircle + 21*34 - circle
print(semicircle,r,circle,shaded)