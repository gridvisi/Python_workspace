'''
https://www.codewars.com/kata/541103f0a0e736c8e40011d5/train/python
@test.describe("Disgruntled Employee")
def test_group():
    @test.it("Fixed tests")
    def test_case():
        test.assert_equals(off(1), [1])
        test.assert_equals(off(2), [1])
        test.assert_equals(off(4), [1, 4])
        test.assert_equals(off(9), [1, 4, 9])
        test.assert_equals(off(12), [1, 4, 9])

Bobsworth爵士是当地一个数据中心的保管员。正如他所猜测的那样，Bobsworth
最近发现他在为维护该设施倾注了多年的心血后，将在生日当天被解雇。

然而，鲍伯斯沃思有其他计划。

Bobsworth知道在数据中心的断路器箱里有1到n个开关。从第1个开关到第n个开关，
鲍勃首先把每个开关都关掉。再从第一个开关开始，鲍勃又打开了第二个开关。
再一次从第一个开关开始，鲍勃又打开了第3个开关。鲍勃继续这个模式，
直到他翻开第n个开关并进行n次传递。

在Bobsworth的混乱结束时，有多少个开关被关掉了？

该函数应该返回一个升序数组，其中包含鲍勃完成复仇后仍然关闭的所有开关号码。
'''


def off(n):
    nls = [True]*n
    for step in range(2,n+1):
        nls = [not(e) if i in (range(step,n+1,step)) else e for i,e in enumerate(nls)]
    return [range(1,n+1)[i] for i,e in enumerate(nls) if e==True]
print(off(9))


def off(n):
    return [i * i for i in range(1, int(n ** 0.5) + 1)]