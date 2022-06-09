#https://www.codewars.com/kata/56e67d6166d442121800074c/train/python
def draw(waves):
    chart = ''
    for j in range(max(waves), 0, -1):
        for i in waves:
            if j > i: chart += '□'
            else: chart += '■'
        chart += '\n'
    return chart[:-1]
waves = [1,2,3,3,2,1,1,2,3,4,5,6,7]
print(draw(waves))