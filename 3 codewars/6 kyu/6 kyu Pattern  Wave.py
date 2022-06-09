'''
https://www.codewars.com/kata/56e67d6166d442121800074c
'''

def draw(waves):
    chart = ''
    for j in range(max(waves), 0, -1):
        for i in waves:
            if j > i: chart += '□'
            else: chart += '■'
        chart += '\n'
    return chart[:-1]

def draw(waves):
    m       = max(waves)
    rotHist = [ ('■'*v).rjust(m, '□') for v in waves ]
    return '\n'.join( map(''.join, zip(*rotHist)) )

def draw(waves):
    m = max(waves)
    return "\n".join("".join("□" if n < (m - row) else "■" for n in waves) for row in range(m))
waves = [1,2,3,4]
waves = [1,2,3,3,2,1]
waves = [5,3,1,2,4,6,5,4,2,3,5,2,1]
#waves = [1,0,1,0,1,0,1,0]
print(draw(waves))



'''
str = 'abcdefg'
for word in str:
    # print(word) # a/n b/n c/n d/n e/n f/n g/n
    #print(word, end='')
    print(f"{word}")
'''

