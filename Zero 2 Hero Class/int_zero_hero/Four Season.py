import math
def season(month):
    return math.ceil(month/3)
month = [season(i) for i in range(1,13)]
print(month)

def season(month):
    return int(str(month),8)

def season(month):
    return [i for i in range(1,13,3)]
month = 6
print(season(month))