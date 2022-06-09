
print("String".lower())
print("String".upper())
print("ring".upper())

light = 'yellow'

if light == 'green':
    print('car pass though asap!')

if light == 'red':
    print('car stop')

'if season is summer, we go swimming, air-conditional,icecream'
"if season is winter, we play snowball "
"if season is spring, we are not snake, play golf and planting tree,"

print('spring:',"plent tree")

eric = ['eric', ' lj','running' , 'blue', 17,  'cs',  'apple',  '蜂鸟','海豚', 'rat' ]
print(eric[9] == eric[-1])
print(eric[9],eric[-1])
'''
classmate = []
four_leg = [] #classmate, four_leg
'''

#def zodiac(name,zodiac):
def zodiac(name, z):
    animal = [ 'rat', "ox", "tiger", "rabbit",
    'dragon', 'snake', 'horse', 'goat',
    'monkey', 'rooster', 'dog', 'pig']
    num = len(animal)
    for person in animal:
        if z in animal:
            return 'i am ' + z
        else:return z + 'is not zodiac'

name, z = 'tan','rabbit'  # 用zodiac而不是z，那么变量名zodiac与函数名zodiac(name,zodiac)冲突，不好！！
print(zodiac(name,z))