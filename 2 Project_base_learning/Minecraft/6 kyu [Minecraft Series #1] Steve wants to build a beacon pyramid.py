'''
https://www.codewars.com/kata/5839cd780426f5d0ec00009a/train/python
Python中字典合并的四种方法
Test.assert_equals(blocks_to_collect(1), {"total": 9, "gold": 9, "diamond": 0, "emerald": 0, "iron": 0})
Test.assert_equals(blocks_to_collect(2), {"total": 34, "gold": 9, "diamond": 25, "emerald": 0, "iron": 0})
Test.assert_equals(blocks_to_collect(3), {"total": 83, "gold": 9, "diamond": 25, "emerald": 49, "iron": 0})
'''

re = {'total': 9, 'gold': 9, 'diamond': 0, 'emerald': 0, 'iron': 0}

def blocks_to_collect(level):
    #raw = {'gold': 0, 'diamond': 0, 'emerald': 0, 'iron': 0}
    result = {}
    raw = ['gold', 'diamond', 'emerald', 'iron']
    re = [0]*len(raw)
    for i in range(level):
        re[i%len(raw)] += (2*(i//len(raw))*len(raw)+3 + (i%len(raw))*2)**2
    result['total'] = sum([i for i in re])
    res = dict(zip(raw,[i for i in re]))
    out = dict(result,**res)
    return out

level = 5
print(blocks_to_collect(level))

#solution 1st
def blocks_to_collect(level):
    answer = {
        'total': sum([(i + 3 + i) ** 2 for i in range(level)]),
        'gold': sum([(i + 3 + i) ** 2 for i in range(0, level, 4)]),
        'diamond': sum([(i + 3 + i) ** 2 for i in range(1, level, 4)]),
        'emerald': sum([(i + 3 + i) ** 2 for i in range(2, level, 4)]),
        'iron': sum([(i + 3 + i) ** 2 for i in range(3, level, 4)]),
    }

    return answer

#solution 2nd
from itertools import count, cycle, islice
BLOCKS = ["gold", "diamond", "emerald", "iron"]
def blocks_to_collect(level):
    result = dict.fromkeys(BLOCKS, 0)
    for block, n in zip(islice(cycle(BLOCKS), level), count(3, step=2)):
        result[block] += n ** 2
    return {**result, "total": sum(result.values())}

#solution 3rd

def blocks_to_collect(height):
    stuff = [0, 0, 0, 0]
    for level in range(height):
        stuff[level % 4] += (2 * level + 3)**2
    return dict(zip(("gold", "diamond", "emerald", "iron", "total"), stuff + [sum(stuff)]))