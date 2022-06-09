#多少对二位数之差是50

def minus_50(x):
    cunt = 0
    for i in range(10,100):
        if len(str(i + x)) == 2:
            cunt += 1

    return cunt
x = 50
print(minus_50(x))


'''
2018 k-5-6
5. What is the least number of times we have to roll a regular die to be sure that at least
one number will be repeated? (Die is the singular form of dice).
Berapa bilangan lemparan dadu paling sedikit yang perlu dibuat supaya dapat dipastikan
sekurang-kurangnya satu nombor akan berulang?
'''
import random
No_repeat_possible_rate = 5/6
#start = No_repeat_possible_rate
#start *= (side - i)/side

start = 1
side = 6
res = []
for i in range(1,100):
    x = random.choices([i for i in range(1,7)])[0]
    print(x)
    if x not in res:
        res.append(x)
    elif x in res:
        print(x,res)
        break



'''
for i in range(1,100):
    res.append(random.choices([i for i in range(1,7)][0]))
    if len(set(res)) < len(res):
        print(i)
'''
