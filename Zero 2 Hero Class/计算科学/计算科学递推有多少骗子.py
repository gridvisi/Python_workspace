'''
计算机科学二级

10人站成一队，他们要么会撒谎，要么会说真话，他们每个人都知道谁在撒谎，谁在说真话。他们都说："在我前面说谎的人比在
我后面说真话的人多①"。

问题是最多有几人是说真话的？

分析：想到第一个前面没有人，说明排在最前面的是个骗子。现在想想最后一个人，在最后一个人的前面至少有一个骗子，而在他
的后面没有人，也可以说没有真话的人，这说明他说的是真话。

再想想如果第二个人说的是真话，满足"在我前面说谎的人比在我后面说真话的人多"，就意味者第二人后面说真话的人应该少于一
个，即等同于没有说真话的。而如前所述已经确定最后一个人说真话，这就产生矛盾！所以，第二人也是说谎。

继续假设第三个人说真话，那么第4-9个人说假话才能满足条件 ①
但立刻得出第4个人说的是真话，因为在第4人之前有2个说谎的，而在他之后只有一个真话，这不是谎话。由此可见，第三个人只
可能是说慌，才能严格满足①

至此，确定了第1-3都是说慌。再看第4人如果说的是真话，那么他之前说谎的人有3个，他之后说真话的必须小于3，即第5-9之
间最多只能有一个说真话，因为最后也就是第10个已经肯定是说真话的。分几种情况讨论：

1、假设4说真话，5 - 9说假话，10说真话。迅速发现第5人出现矛盾，因为第5人前面说慌的人的确要多于他后面说真话的。
所以，以上假设不成立。

2、假设4，5都是说真话，那么第6个人前面有3个假话和2个真话，第6个人后面只能有1个真话即第10位。说明第6人说的是真
话，因为满足①，但这样以来，矛盾出现：4，5，6都是真话，意味着第4人前面有3个说慌的，后面有3个说真话的，又与①矛盾

3、假设4说真话，5说假话，6说真话，7-9说假话。还是与1一样出现矛盾！

综合以上3种情况概括推断第4个人也只能是说慌的。

那么第5人呢？
假设第5人说真话，已断定前面4人都是假话，如果假设6-9全是假话，立刻产生矛盾，即第6人说的又为真。如果坚持5说真话，
6也是真话，第4人的断言又变为真

推知5也是假话！

那么第6人呢？①
假设第6人断言为真，为了满足①，7-10最多可以有4个为说真话的，即7-10可以全部都是说真话的。7-10之间可否存在说谎的呢？
答案是否定的。假定7说慌，但发现7之前有5个说慌的，7之后有3个说真话的，符合并满足①，说明7没有说慌！

综上所述，1-5说谎，6-10说真话。
'''

person = [0,0,0,0,0,1,1,1,1,1]
print(all((person[:i].count(0) > person[i+1:].count(1)) == e for i,e in enumerate(person)))

person = [1 for _ in range(10)]
#print(person)
#person[0] = 0
#person[-1] = 1
i = 0
while True:
    if person[:i].count(0) < person[i:].count(1):
        person[i] = 0
    elif person[:i].count(0) > person[i:].count(1):
        if all((person[:i].count(0) > person[i+1:].count(1)) == e for i,e in enumerate(person)):
            print(person)
        break
    i += 1
