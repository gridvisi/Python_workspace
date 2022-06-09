'''
https://www.codewars.com/kata/5c8bfa44b9d1192e1ebd3d15/train/python

test.assert_equals(warn_the_sheep(['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep', 'sheep']), 'Oi! Sheep number 2! You are about to be eaten by a wolf!')
test.assert_equals(warn_the_sheep(['sheep', 'wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']), 'Oi! Sheep number 5! You are about to be eaten by a wolf!')
test.assert_equals(warn_the_sheep(['wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']), 'Oi! Sheep number 6! You are about to be eaten by a wolf!')
test.assert_equals(warn_the_sheep(['sheep', 'wolf', 'sheep']), 'Oi! Sheep number 1! You are about to be eaten by a wolf!')
test.assert_equals(warn_the_sheep(['sheep', 'sheep', 'wolf']), 'Pls go away and stop eating my sheep')
'''
print([i for i in range(1,11)])
animal = ['rat', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep', 'sheep', 'cat']

print('slice 数组切片：',animal[::-1])


animal = ['sheep', 'sheep', 'sheep','wolf']
animal.extend(['sheep','sheep'])
animal.append('cat')
print('new:',animal)

wolf_position = animal.index('wolf')
end = len(animal) - 1

print('rest of wolf:',wolf_position,end,end - wolf_position)

print(animal[-2])
print(animal[0],animal[-1],animal.index('wolf'))
print(animal.insert(0,'rat'))

print('2nd=second:',animal)
animal.remove('sheep')
animal.remove('sheep')
animal.remove('sheep')
print('倒过来：',animal[::-1])


print('3rd= third:',animal)
print('count',animal.count('sheep'))

print(len(animal)) #length
print('狼是否在队伍的尾部：',len(animal) == animal.index('wolf'))
#Bool :True False
print("wolfs position:",animal.index('wolf'))

# by ericlee
def warn_the_sheep(queue):
    for i in range(len(queue)):
        if i != len(queue)-1 and queue[i] == 'wolf':
            return f"Oi! Sheep number {len(queue)-i-1}! You are about to be eaten by a wolf!"
    else:
        return "Pls go away and stop eating my sheep"


def warn_the_sheep(queue):
    if queue.index('wolf') < len(queue) - 1:
        x = len(queue) - queue.index('wolf') -1
        return f"Oi! Sheep number {x}! You are about to be eaten by a wolf!'"
    return 'Pls go away and stop eating my sheep'
queue = ['wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']
print(warn_the_sheep(queue))


#1st solution
def warn_the_sheep(queue):
    n = len(queue) - queue.index('wolf') - 1
    return f'Oi! Sheep number {n}! You are about to be eaten by a wolf!' if n else 'Pls go away and stop eating my sheep'


#2
def warn_the_sheep(queue):
    i = queue[::-1].index('wolf')
    if i == 0:
        return 'Pls go away and stop eating my sheep'
    return f'Oi! Sheep number {i}! You are about to be eaten by a wolf!'