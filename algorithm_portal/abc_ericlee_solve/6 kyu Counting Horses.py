'''
https://www.codewars.com/kata/5f799eb13e8a260015f58944/train/python
A group of horses just ran pass Farmer Thomas, and he would like to figure out how many
horses were there. However, Farmer Thomas has a bad eye sight, and cannot really see the
horses that are now distant. He did remember the sound of their galloping though, and
he wants your help in figuring out how many horses (and the length of their legs)
were in that group.

Each horse will make a thumping noise every step as its hooves hit the ground. Farmer
Thomas has recorded the sound as strings like this (the following record is 15 seconds long):

000100010001000
where each number represents how many thumps he heard in that second.

However, there's a catch; horses with longer legs take bigger steps, resulting in longer
intervals between thumps. Specifically, a horse with leg length n will thump every n seconds.

A single horse with leg length 2 will sound like:

01010101010101
The same rule applies when there are multiple horses. Two horses with
leg length 2 and 3 sound like:

0111020111
Note that the sixth digit is 2 since both horses thump in that second.

Input
A string of any length that represents the sound of the horses' galloping
(as described above).

Output
An array of length equivalent to the amount of horses where each element
represents the leg length of a horse.

For example, this input

0111020111
should return [2, 3].

Notes
There could be multiple horses with the same leg length. 0020020020020 is the sound of 2 horses, both of which have leg length of 3.

一群马刚刚跑过农夫托马斯，他想弄清楚有多少马。但是，农夫托马斯的眼睛视力不好，无法真正看到现在远处的马匹。
不过他还记得他们奔跑的声音，他希望你能帮助他算出那群马有多少匹（以及它们的腿长）。

每匹马每走一步，蹄子落地时都会发出砰砰的声音。农夫托马斯把声音记录成了这样的字符串（以下记录长15秒）。

000100010001000
其中每个数字代表他在那一秒内听到的砰砰声有多少。

然而，有一个问题，腿长的马迈的步子更大，导致怦然心动的间隔时间更长。具体来说，一匹腿长为n的马，
每n秒就会有一次怦然心动。

一匹腿长为2的马，声音就会像。

01010101010101
当有多匹马时，同样的规则也适用。两匹马的腿长2和3听起来像。

0111020111
请注意，第六位数是2，因为这两匹马都在那一秒内砰砰作响。

輸入:一个任意长度的字符串，表示马匹奔跑的声音（如上所述）。

輸出:一个长度相当于马匹数量的数组，每个元素代表一匹马的腿长。

例如，这个输入0111020111 该返回[2, 3]。

注释:腿长相同的马可能有多匹。0020020020020是2匹马的声音，这2匹马的腿长都是3。
所有马匹的怦然心动周期在声音串开始时是同步的。这意味着你不必担心相位偏移的问题。
声音串的长度总是大于最长的腿长（意味着每匹马都会在串中至少跳一次）。
你的输出将在测试中进行排序，以便比较（你的答案不需要排序）。

from solution import count_horses
import codewars_test as test

@test.describe("Counting Horses")
def tests():
    # Use "it" to identify the conditions you are testing for
    @test.it("Example Cases")
    def horses_test():
        test.assert_equals(sorted(count_horses('010101010')), [2])
        test.assert_equals(sorted(count_horses('00000000')), [])
        test.assert_equals(sorted(count_horses('0001000100010001000100')), [4])
        test.assert_equals(sorted(count_horses('11111')), [1])
        test.assert_equals(sorted(count_horses('0111020111')), [2, 3])
        test.assert_equals(sorted(count_horses('0212030212')), [2, 2, 3])
        test.assert_equals(sorted(count_horses('122213122213122')), [1, 2, 3])
'''
def count_horses(sound_str):
    i,ans = 0,[]
    start = [int(i) for i in sound_str]
    while start and i < len(start):
        minus = start[i]
        ans.append((i+1,start[i]))
        d = [i for i in range(len(start))]
        sl = d[i::i + 1]
        #print(start)
        #print(ans,slic,start,minus)
        start = [v-minus if k in sl else v for k,v in enumerate(start)]
        if sum(start) == 0:
            res = [[i[0]] * i[1] for i in ans if i[1]]
            return [x for arr in res for x in arr]
        i += 1
sound_str = '122213122213122'
#sound_str = '0212030212'
#sound_str = '122213122213122'
#sound_str = '010101010'
#sound_str = '0001000100010001000100'
print('Solution 1st:',count_horses(sound_str))
print('input:',list(sound_str))
'''
Time: 8858ms Passed: 760 Failed: 0
Test Results:
 Counting Horses
 Trivial Test Cases (10 of 10 Assertions)
 Random Test Cases (500 of 500 Assertions)
 Large Random Test Cases (250 of 250 Assertions)
Completed in 8020.10ms
'''
#1st solution
def count_horses(sound_str):
    res = []
    for i, n in enumerate(map(int, sound_str), 1):
        res += [i] * (n - sum(1 for s in res if i % s == 0))
    return res

#2nd solution  dict
def count_horses(s):
    a = list(map(int,s))
    d,r = {},[]
    for i,v in enumerate(a,1):
        if v:
            x = sum(k for j,k in d.items() if not i%j)
            if v-x:
                d[i] = v-x
                r.extend((v-x)*[i])
    return r

#3th solution
def count_horses(sound_str):
    horses,xn=[],[int(c) for c in sound_str]
    l=len(xn)
    for i,c in enumerate(xn):
        if c==0: continue
        for j in range(i,l,i+1):xn[j]-=c
        horses+=[i+1]*c
    return horses

#4th solution
def count_horses(sound_str):
    # convert to list of ints so we can do math
    sound_lst = [int(x) for x in sound_str]

    horses = []
    while sum(sound_lst) > 0:  # while still horses
        for x in range(len(sound_lst)):  # find first number > 0
            if sound_lst[x] != 0:  # found horse, remove all steps
                horses.append(x + 1)
                for y in range(x, len(sound_lst), x + 1):
                    sound_lst[y] = sound_lst[y] - 1
                break  # get out of the for loop

    return horses


start,i = '12232312',2
d = list(range(len(start)))
#slic = list(range(len(start)))[i::i + 1]
slic = d[i::i + 1]
#print(slic,[e for i,e in enumerate(start) if i in slic])

from collections import Counter
def count_horses(sound_str):
    i,ans = 0,[]
    start = [int(i) for i in sound_str]
    while start and i<len(start):
        minus = start[i]
        ans.append((i+1,start[i]))
        d = [i for i in range(len(start))]
        sl = d[i::i + 1]
        print(start)
        #print(ans,slic,start,minus)
        for k, v in enumerate(start):
            if k in sl:
                start[k] = v - minus
            else:
                pass #start[k] = v
             #start = [(v-minus) if k in slice else v]
        if sum(start) == 0:
            res = [[i[0]] * i[1] for i in ans if i[1]]
            return [x for arr in res for x in arr]
        i += 1
#return ans  #[x for arr in res for x in arr]
'''
Time: 8592ms Passed: 760 Failed: 0
Test Results:
 Counting Horses
 Trivial Test Cases (10 of 10 Assertions)
 Random Test Cases (500 of 500 Assertions)
 Large Random Test Cases (250 of 250 Assertions)
Completed in 7768.92ms
You have passed all of the tests! :)
'''
sound_str = '122213122213122'
#sound_str = '0212030212'
#sound_str = '122213122213122'
#sound_str = '010101010'
#sound_str = '0001000100010001000100'
#print('Solution 1st:',count_horses(sound_str))
#print('input:',list(sound_str))


# The dict solution work try again:
def count_horses(sound_str):
    start = [int(i) for i in sound_str]
    soundDict = dict([(int(i),int(e)) for i,e in enumerate(sound_str)])
    ans = []
    for i,e in enumerate(start):
        prev = soundDict[i]
        ans.append((i+1, prev))
        print('ans:',ans)
        for k,v in soundDict.items():
            if k in list(range(len(start)))[i::i + 1]:
                soundDict[k] -= prev
        print(soundDict)
        if all(v==0 for k,v in soundDict.items()):
            res = [[i[0]] * i[1] for i in ans if i[1]]
            return [x for arr in res for x in arr]  #,soundDict

#[x for arr in result for x in arr]
# [int(i) for i in result] # output是大坑啊

#sound_str = '122213122213122'
sound_str = '0212030212'
sound_str = '122213122213122'
#sound_str = '010101010'
#sound_str = '0001000100010001000100'

'''
Passed: 352 Failed: 0 Exit Code: 1
Test Results:
 Counting Horses
 Trivial Test Cases (10 of 10 Assertions)
 Random Test Cases (342 of 342 Assertions)
 STDERR
Execution Timed Out (12000 ms)
'''
def count_horses(sound_str):
    ans = []
    start = [int(i) for i in sound_str]
    for i in range(len(start)-1):
        ans.append([i+1,start[i]])
        #print(list(range(len(start))[::i+1]))
        start = [e - start[i] if d in list(range(len(start))[i::i+1]) else e for d,e in enumerate(start)]
        #print(start)
        result = [[i[0]] * i[1] for i in ans if i[1]]
    return [x for arr in result for x in arr]       # [int(i) for i in result] # output是大坑啊
'''
Passed: 352 Failed: 0 Exit Code: 1
Test Results:
 Counting Horses
 Trivial Test Cases (10 of 10 Assertions)
 Random Test Cases (342 of 342 Assertions)
 STDERR
Execution Timed Out (12000 ms)
'''
sound_str = '122213122213122'
sNum = [int(i) for i in sound_str]
i = 1
print(sNum[::i])

from collections import Counter
def count_horses(sound_str):
    rythm = Counter(sound_str)
    res = dict([(k,[]) for k,v in Counter(sound_str).items()])
    for k in set(list(sound_str)):
        res[k] = [i for i,e in enumerate(sound_str) if k <= e]
    #rythm = [i for i,e in enumerate(sound_str) if i in sorted(set(list(sound_str)))]
    return res,rythm


def count_horses(sound_str):
    ans = []
    tita = [int(i) for i in sound_str]
    for k in sorted([int(i) for i in set(list(sound_str))],reverse=True):
        #print(ans,tita,sorted([int(i) for i in set(list(sound_str))]))
        ans.append([((k,i),(e - k)) for i,e in enumerate(tita) if i%k == 0])
    return ans
#sound_str = '122213122213122'
#print('Solution 2nd:',count_horses(sound_str))

def count_horses(sound_str):  # Not good
    start = [int(i) for i in sound_str]
    i,step,sNum = 1,[],start[:]
    while len(step) < max(start):
        prev = len(start)
        sNum = [n-1 for n in sNum[::i] if n-1 >= 0]
        #print(step, sNum, len(sound_str), i)
        print(sNum)
        if len(sNum) == prev:
            step.append(i)
        else:
            sNum = start[:]
            i += 1
    return step

def count_horses(sound_str):        # Not good
    start = [int(i) for i in sound_str]
    step,sNum,st = [],start[:],0
    print(sNum)
    i = 0
    while i < max(start):
        print(sNum[0])
        if start[0] == 1:
            #st += 1
            step.append(1)
            #print('step:',step)
        else:
            #prev, sNum = len(sNum),[n-1 for n in start[st::st]]
            #print(step, sNum)

            #st += 1
            sNum = [n-1 for n in start[st+1::st+2]]
            a = [i for i in sNum]
            b = [i for i in sNum if i >= 0]
            print('2nd:',st,sNum,step,a,b)

            if len(a) == len(b):
                #st += 1
                step.append(st+2)

            #sNum = start[:]
        i += 1

    return step

# super cool summary:
res = [1]
res = [3,2]
print('[]:',list(1 for s in res if 1%s==0))
res = [2]
i = 1
x = list((1 for s in res if i % s == 0))
print('super cool summary:',sum(1 for s in res if i % s == 0),x)

def count_horses(sound_str):
    res = []
    #'0212030212'
    for i, n in enumerate(map(int, sound_str), 1):
        print('list:',list((1 for s in res if i % s == 0)))
        res += [i] * (n - sum(1 for s in res if i % s == 0))
        print(res,[i])
    return res
sound_str = '122213122213122'
sound_str = '0212030212'
#sound_str = '122213122213122'
#sound_str = '010101010'
#sound_str = '0001000100010001000100'
print('Solution 1st:',count_horses(sound_str))
print('input:',list(sound_str))

print([(i,e) for i,e in enumerate(map(int,'313312'),1)])
print([(i,e) for i,e in enumerate(map(int,'313312'),0)])