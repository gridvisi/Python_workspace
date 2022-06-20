
# Fractor circle

def numCircles(n):
    if n == 1: return 1
    return numCircles(n - 1) * 3 + 1
n = 4
print(numCircles(n))

