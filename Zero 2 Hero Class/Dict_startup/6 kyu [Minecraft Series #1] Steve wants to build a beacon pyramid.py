'''
https://www.codewars.com/kata/5839cd780426f5d0ec00009a/train/python

test.assert_equals(blocks_to_collect(1), {"total": 9, "gold": 9, "diamond": 0, "emerald": 0, "iron": 0})
test.assert_equals(blocks_to_collect(2), {"total": 34, "gold": 9, "diamond": 25, "emerald": 0, "iron": 0})
test.assert_equals(blocks_to_collect(3), {"total": 83, "gold": 9, "diamond": 25, "emerald": 49, "iron": 0})
'''
# 每次几盘三文鱼
rule = {"gold": 0, "diamond": 0, "emerald": 0, "iron": 0}
rule['gold'] = 0
for k,v in rule.items():
    v += 1
    print(k,v)

for k,v in rule.items():
    v += 1
print(k,v)

# for loop
l,start,level,total = 0,3,3,0
rule = {"gold": 0, "diamond": 0, "emerald": 0, "iron": 0}
while l <= level:
    cunt = start
    for k,v in rule.items():
        rule[k] += cunt*cunt
        cunt += 2
        l += 1
        #print('-',k,v)
        if l == level:
            total = {'total':sum([v for k,v in rule.items()])}
            total.update(rule)
            print('while', total,rule)
    start = cunt


# eric_solution rank#11
def blocks_to_collect(level):
    l,start = 0,3
    rule = {"gold": 0, "diamond": 0, "emerald": 0, "iron": 0}
    while l <= level:
        cunt = start
        for k, v in rule.items():
            print('-', k, v)
            rule[k] += cunt * cunt
            cunt += 2
            l += 1
            if l == level:
                total = {'total':sum(list(rule.values()))}
                total.update(rule)
                return total
        start = cunt
level = 5
print('def',blocks_to_collect(level))

def blocks_to_collect(level):
    rule = {"gold": 0, "diamond": 0, "emerald": 0, "iron": 0}
    # key=str  value=int
    n = iter(list(range(3,level)))
    print(n)
    for k,v in rule.items():
        rule[k] = n**2
        next(n)
        print(n)
    return rule

level = 4
#print(blocks_to_collect(level))


#1st
def blocks_to_collect(level):
    answer = {
        'total': sum([(i + 3 + i) ** 2 for i in range(level)]),
        'gold': sum([(i + 3 + i) ** 2 for i in range(0, level, 4)]),
        'diamond': sum([(i + 3 + i) ** 2 for i in range(1, level, 4)]),
        'emerald': sum([(i + 3 + i) ** 2 for i in range(2, level, 4)]),
        'iron': sum([(i + 3 + i) ** 2 for i in range(3, level, 4)]),
    }

    return answer