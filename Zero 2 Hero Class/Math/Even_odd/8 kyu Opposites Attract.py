'''
https://www.codewars.com/kata/555086d53eac039a2a000083/train/python
'''

print(sum([i for i in range(11) if i%2 == 0]))

flower1,flower2 = 1,9

def lovefunc( flower1, flower2 ):
    return flower1 != flower2
print(lovefunc(flower1,flower2))

def lovefunc( flower1, flower2 ):
    return bin(flower1)[0] != bin(flower2)[0]
print(lovefunc(flower1,flower2))

def lovefunc( flower1, flower2 ):
    return bin(flower1)[-1] != bin(flower2)[-1]
print(lovefunc(flower1,flower2))