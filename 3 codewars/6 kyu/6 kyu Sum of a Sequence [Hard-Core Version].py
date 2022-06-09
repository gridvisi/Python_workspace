'''
https://www.codewars.com/kata/587a88a208236efe8500008b/train/python

正如标题所暗示的那样，这是另一个整齐的卡塔的硬核版本。

任务很简单：简单的将所有的数字相加，从第一个参数为起点到第二个参数为上限（可能包括在内），
按第三个参数表示的步骤进行。

sequence_sum(2, 2, 2) # 2
sequence_sum(2, 6, 2) # 12 (= 2 + 4 + 6)
sequence_sum(1, 5, 1) # (= 1 + 2 + 3 + 4 + 5)
sequence_sum(1, 5, 3) # 5 (= 1 + 4)
如果它是一个不可能的序列(开头大于结尾，并且是正步或反过来)，只需返回0。更多的例子请看提供的测试案例:)

注意：与其他基础卡塔不同，更大的范围将被测试，所以你应该希望让你的algo得到优化，并避免强行通过解决方
案的方式。
'''
#1st solution math!!!
def sequence_sum(a, b, step):
    n = (b-a)//step
    return 0 if n < 0 else (n+1)*(n*step+a+a)//2
# 高斯法

#2nd solution
def sequence_sum(b, e, s):
    q, r = divmod(e - b, s)
    return (b + e - r) * max(q + 1, 0) // 2

#3rd solution
def sequence_sum(start, stop, step):
    n = (stop - start) // step
    last = start + n * step
    return (n+1) * (start + last) // 2 if n >= 0 else 0

#4h solution
def sequence_sum(b, e, s):
    if (s > 0 and b > e) or (s < 0 and b < e):
        return 0
    near = e - (e - b) % s
    n = (near - b) // s + 1
    return (b + near) * n // 2

def Fibonacci_Yield_tool(n):
    a, b = 0, 1
    while n > 0:
        yield b
        a, b = b, a + b
        n -= 1
print(list(Fibonacci_Yield_tool(5)))

def sequence_sum(begin_number, end_number, step):
    ans = 0
    while begin_number <= end_number:
        #yield ans
        begin_number,ans = begin_number+step,ans+begin_number
    return ans  #,begin_number

# 效率性能不佳
begin_number, end_number, step = 20, 673388797, 5  #45345247259849570
begin_number, end_number, step = 9383, 71418, 2  #1253127200
print(sequence_sum(begin_number, end_number, step))
#print(list(sequence_sum(begin_number, end_number, step))[-1])


def sequence_sum(begin_number, end_number, step):
    ans = 0
    it = iter(range(begin_number, end_number+1, step))
    round = int((end_number - begin_number)/step)
    round1 = (end_number - begin_number)//step
    print(round,round1)
    if round == 0:
        return begin_number

    elif round > 0:
        for i in range(round):
            ans += next(it)
        return ans
#begin_number, end_number, step = 20, 673388797, 5  #45345247259849570
#begin_number, end_number, step = 780, 6851543, 5  #4694363402480
#begin_number, end_number, step = -2, 4, 658
#begin_number, end_number, step = 9383, 71418, 2  #1253127200
begin_number, end_number, step = 2, 6, 2  #12
#print(sequence_sum(begin_number, end_number, step))

it = iter(range(begin_number,end_number,step))

def sequence_sum(begin_number, end_number, step):
    ans = 0
    it = iter(range(begin_number, end_number+1, step))
    while True:
        try:
            ans += next(it)
        except StopIteration:
            # 遇到StopIteration就跳出循环, 且自动频闭StopIteration异常
            break
    return ans
begin_number, end_number, step = 9383, 71418, 2  #1253127200
#begin_number, end_number, step = 2, 6, 2  #12
#begin_number, end_number, step = 20, 673388797, 5  #45345247259849570
#print(sequence_sum(begin_number, end_number, step))



def sequence_sum(begin_number, end_number, step):
    if end_number - begin_number < step and end_number > begin_number:
        return begin_number
    elif end_number < begin_number and step > 0:
        return 0
    elif step < 0 or step > 0:
        m = divmod(end_number - begin_number,step)[0] + 1
        mid = begin_number + end_number - divmod(end_number - begin_number,step)[1]
        if m % 2 == 0:
            return (mid * m)/2
        if m % 2 == 1:
            return int((mid * (m - 1)/2) + begin_number + (m - 1)*step/2)

