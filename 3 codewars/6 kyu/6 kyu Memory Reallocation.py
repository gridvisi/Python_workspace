'''
https://www.codewars.com/kata/5ad927c932d79e34fb000091/train/python
您的服务器有16个内存库；每个内存库可以容纳任意数量的块。您必须编写一个例程来平衡内存库之间的块。
重新分配例程按周期运行。在每个周期中，它都会找到块数最多的内存库（由数量最少的内存库获得的连接），并在这些内存库之间重新分配这些块。为此，它将从选定的存储库中删除所有块，然后移动到下一个（按索引）存储库并插入其中一个块。它继续这样做，直到块用完为止；如果它到达最后一个内存库，它就会绕到第一个内存库。
我们需要知道在生成之前已经看到的银行配置中的块之前，可以执行多少次重新分配。
例如，假设一个场景只有四个内存库：
库以0、2、7和0块（[0,2,7,0]）开始。第三个银行拥有最多的区块（7个），因此选择它进行重新分配。
从下一个存储组（第四个存储组）开始，然后一次继续一个块，这7个块分布在存储组上。第四、第一和第二家银行各获得两个街区，第三家银行获得一个街区。最终结果如下：2 4 1 2。
接下来，选择第二个库，因为它包含最多的块（四个）。因为有四个内存库，每个都有一个块。结果是：3 1 2 3。
现在，第一和第四个内存库之间有了联系，它们都有三个块。第一家银行赢得了平局，它的三个街区平均分布在其他三家银行，没有留下：0 2 3 4。
第四个银行被选中，其四个区块被分配，使得四个银行中的每一个都得到一个：1 3 4 1。
第三个银行被选中，同样的事情发生了：2 4 1 2。在这一点上，我们已经达到了我们以前见过的状态：2 4 1 2已经见过了。无限循环是在第五个块重新分配循环之后检测到的，因此本例中的答案是5。
返回在生成以前看到的配置之前完成的重新分发周期数。

人们似乎在挣扎，下面是对上述示例的一个可视化演练：http://oi65.tinypic.com/dmshls.jpg
注意：记住，内存访问非常快。你的应该也是。
给那些超时的人的提示：看看即使在样本测试中也发生的循环数。这是很多不同的配置，很多不同的时间，你会寻找一个匹配的序列。想办法减少搜索过程所需的时间。
如果你喜欢，请投赞成票！:)
The banks start with 0, 2, 7, and 0 blocks ([0,2,7,0]).
The third bank has the most blocks (7), so it is chosen for redistribution.
Starting with the next bank (the fourth bank) and then continuing one block at a time,
the 7 blocks are spread out over the memory banks.
The fourth, first, and second banks get two blocks each, and the third bank gets one back.
The final result looks like this: 2 4 1 2.
Next, the second bank is chosen because it contains the most blocks (four).
Because there are four memory banks, each gets one block. The result is: 3 1 2 3.
Now, there is a tie between the first and fourth memory banks, both of which have three blocks.
The first bank wins the tie, and its three blocks are distributed evenly over the other three banks,
leaving it with none: 0 2 3 4.
The fourth bank is chosen, and its four blocks are distributed such that each of the four banks
receives one: 1 3 4 1.
The third bank is chosen, and the same thing happens: 2 4 1 2. At this point,
we've reached a state we've seen before: 2 4 1 2 was already seen.
The infinite loop is detected after the fifth block redistribution cycle,
and so the answer in this example is 5.

Test.assert_equals(mem_alloc([5, 1, 10, 0, 1, 7, 13, 14, 3, 12, 8, 10, 7, 12, 0, 600]), 70)
Test.assert_equals(mem_alloc([53, 21, 10, 0, 1, 7, 13, 14, 3, 12, 8, 10, 7, 12, 0, 60]), 316)
Test.assert_equals(mem_alloc([14, 21, 10, 0, 1, 7, 0, 14, 3, 12, 8, 10, 17, 12, 0, 19]), 826)
Test.assert_equals(mem_alloc([5, 1, 10, 0, 1, 7, 13, 14, 3, 12, 8, 10, 7, 12, 0, 6]), 5042)
Test.assert_equals(mem_alloc([17, 17, 3, 5, 1, 10, 6, 2, 0, 12, 8, 11, 16, 2, 1, 6]), 158378)
'''
banks = [5, 1, 10, 0, 1, 7, 13, 14, 3, 12, 8, 10, 7, 12, 0, 600]  #70
def mem_alloc(banks):
    seen = set()
    while tuple(banks) not in seen:
        seen.add(tuple(banks))
        print(seen)
        number = max(banks)
        index = banks.index(number)
        banks[index] = 0
        while number:
            index = (index + 1) % 16  # len(banks)?
            banks[index] += 1
            number -= 1
    return len(seen)

print(mem_alloc(banks))