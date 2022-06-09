def zodiac(name):
    '''
    animal = ['rat', ox, tiger, rabbit,
    dragon, snake, horse, goat,
    monkey, rooster, dog, pig]
    '''
    animal = ['rat', 'ox', 'tiger', 'rabbit',
    'dragon', 'snake', 'horse', 'goat',
    'monkey', 'rooster', 'dog', 'pig']
    res = []
    num = len(animal)
    my_zodiac = animal[0]
    none_leg = ['snake','dragon']
    two_leg = ['rooster']
    for item in animal:
        if name not in none_leg + two_leg:
            res.append(item)
    four_leg = res
    return four_leg,my_zodiac

name = 'rabbit'
print(zodiac(name))

a,b = 1,2
print(1+2)
print(a + b)
x = a + b  # #为什么这里可以没有x = 0有这句？
print(x)

def total(x):
    zonghe = 0    #为什么必须有这句？
    for i in range(x+1):
        zonghe += i
    return zonghe
x = 100
print(total(x))


