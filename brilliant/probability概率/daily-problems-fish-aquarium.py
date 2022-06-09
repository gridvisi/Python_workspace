'''
https://brilliant.org/daily-problems/fish-aquarium/


'''

# best case: seven fish to be marked respectively,unmarked fish is 3
# worst case: one fish is to be marked 7 times,unmarked fish is 9

import random
def marked_fish(num,cunt):
    #i = 0
    fish = [0] * num
    print(fish)
    for i in range(cunt):
        pick = random.choices(range(num))[0]
        print('pick:',pick)
        print(fish[pick])
        fish[pick] = 1 if fish[pick] == 0 else 1

    return fish.count(0)
num,cunt = 10,7
print('unmarked:',marked_fish(num,cunt))

repeat = 10000
cnt = 0
for i in range(repeat):
    cnt += marked_fish(num,cunt)
print('repeat pick:',cnt/repeat)




'''

pick = random.choice([list(range(num+1))])
pick = random.choices('123456789')
pick = random.choices(list('123456789'))
pick = random.choices(range(10))
print(pick)
'''