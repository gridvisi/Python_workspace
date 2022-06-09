#列表碾平

test_list = [[1, 2], [3, 4]]
from itertools import chain
list(chain.from_iterable(test_list))

from itertools import chain
list(chain(*test_list))

sum(test_list, [])

#[x for y in test_list for x in y]

#递归
func = lambda x: [y for t in x for y in func(t)] if type(x) is list else [x]
func(test_list)

print(1 == 1 and 2 or 3)  # 2
print(1 == 2 and 2 or 3)  # 3
print(2 if 1 == 1 else 3)  # 2
print(2 if 1 == 2 else 3)  # 3