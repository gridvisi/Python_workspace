'''
返回一个CPU级别的精确时间计数值，单位为秒。
代码如下：
import time
start=time.perf_counter()
print("start:",start)
end=time.perf_counter()
print("\nend:",end)
duration=end-start
print("\nThe duration is:",duration)
此代码为获得两次指令之间的持续时间！

代码为本人亲自敲写，都可以运行，转载的朋友请注明出处

作者：泡泡360
链接：https://www.jianshu.com/p/b8b0cc40a181
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

import math
import time
#import per_counter
from numba import njit, prange


@njit(fastmath=True, cache=True)
def is_prime(num):
    if num == 2:
        return True
    if num <= 1 or not num % 2:
        return False

    for div in range(3, int(math.sqrt(num) + 1), 2):
        if not num % div:
            return False
    return True


@njit(fastmath=True, cache=True, parallel=True)
def run_program(N):
    for i in prange(N):
        is_prime(i)

if __name__ == "__main__":
    N = 10000000

start = time.perf_counter()
run_program(N)
end = time.perf_counter()
print(end - start)