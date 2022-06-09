

# 输出一千万内的偶数，比较两种写法的时间效率
import time
#第一种数组切片
start_time = time.time()
num = [i for i in range(0,10000000,2)]
end_time = time.time()
print(end_time - start_time)

#第二种偶数的条件判断
start_time = time.time()
num = [i for i in range(0,10000000) if i % 2 == 0]
end_time = time.time()
print(end_time - start_time)

#0.26999783515930176
#0.755185604095459
#第一种写法耗时是第二种写法的三分之一

from collections import Counter
class Solution:
    def singleNumbers(self, nums):
        d = Counter(nums)
        re = []
        #key = set(sorted(nums))
        for k,v in d.items():
            if d[k] == 1:
                re.append(k)
                if len(re) == 2:
                    return re