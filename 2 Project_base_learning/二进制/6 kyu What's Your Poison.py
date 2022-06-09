'''
https://www.codewars.com/kata/58c47a95e4eb57a5b9000094/train/python

谜语
一个小国家的国王邀请1000名参议员参加他的年度聚会。按照传统，每位参议员都会给国王带来一瓶酒。不久后，
王后发现其中一位参议员正试图通过给国王一瓶有毒的酒来暗杀国王。不幸的是，他们不知道是哪位参议员，也不
知道哪瓶酒被下了毒，毒药完全无法辨别。

然而，国王有10只实验鼠。他决定用它们作为味觉测试者，来确定哪瓶酒中含有毒药。毒药服用后对老鼠没有任何
影响，直到24小时后，被感染的老鼠突然死亡。国王需要在明天之前确定哪瓶酒是有毒的，这样庆典活动才能按计
划进行。

因此，他只有一轮测试的时间，他决定根据一定的方案，让每只老鼠品尝多瓶酒。

你的任务
你收到一个整数组(0-9)，每一个整数都是一只老鼠在品尝酒瓶后死亡的数量。返回被毒死的酒瓶的编号(1...1000)。

祝您好运!
提示：把老鼠看作是酒瓶数量的某种代表......

PUZZLESGALGORITHMS BITS BINARY TERVIEW问题。

test.describe("Basic Tests")
test.assert_equals(find([0,3,5,4,9,8]),825)
test.assert_equals(find([0,1,9,3,5]),555)
test.assert_equals(find([0,1,2,3,4,6]),95)
test.assert_equals(find([0,1,3,4]),27)唯一的组合的死亡也能代表一瓶药有毒。

现在有10只老鼠，那么我们以老鼠的死和排序作为一瓶药的编号。例如：

代表第1瓶药： 0    0     1
代表第2瓶药： 0    1     0
代表第3瓶药： 0    1     1
代表第4瓶药： 1    0     0
代表第5瓶药： 1    0     1
代表第6瓶药： 1    1     0
代表第7瓶药： 1    1     1

第一只老鼠（从右往左数，自上而下）要喝的有1、3、5、7 四瓶药，
第二只老鼠要喝的有2、3、6 三瓶药，
第三只老鼠喝的是4、5、6、7 四瓶药。

第一只老鼠死了代表第一瓶是毒药，第二只死了代表第二瓶是毒药，
第一和第二都死了代表第3瓶是毒药，第三只死了代表第4瓶是毒药，
第一和第三死了代表第5瓶是毒药、、、以此类推


代表第8瓶药： 1    0     0     0
代表第9瓶药： 1    0     0     1

'''
print(bin(555))
print(bin(0b11010))

#10th solution by ericlee
def find(r):
    ans = ['0']*(max(r)+1)
    for i in r:
        ans[max(r)-i] = '1'
    print(ans)
    return int('0b'+''.join(ans),2)
#int('0b' +''.join(['1' if i in r else '0' for i,e in enumerate(ans)][::-1]),2)
r = [0,1,9,3,5]
print(find(r))

#1st
def find(r):
    return sum(2**i for i in r)

#2nd solution
def find(rats):
    """
    The rule the king should use is the following:
        1) Label all bottle from 1 to 1000
        2) Label all rats from 0 to 9
        3) For each rat r, make it drink the bottle b if the binary representation
        of b has it's rth bit is one.
    Reconstruct the label of the poisonned bottle by computing the base-10 representation:
    """
    return sum(map(lambda x: pow(2,x), rats))

#4th
def find(r):
    return sum(1<<d for d in r)


#6
def find(r):
    # Your code here
    rats = [i for i in range(9,-1,-1)]
    bottle = ""
    for rat in rats:
        if rat in r:
            bottle += "1"
        else:
            bottle += "0"
    bottle_number = int(bottle,2)
    return bottle_number