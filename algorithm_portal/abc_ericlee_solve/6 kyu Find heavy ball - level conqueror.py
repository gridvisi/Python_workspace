'''
https://www.codewars.com/kata/54404a06cf36258b08000364/train/python

有8个球，编号从0到7，其中7个球的重量相同。有一个比较重。你的任务是找出它的号码。
https://www.codewars.com/kata/54404a06cf36258b08000364/train/python
你的函数findBall将收到一个参数--scales对象。天平对象包含一个内部存储的8个元素的数组
（索引为0-7），每个元素都有相同的值，只有一个元素更大。
它还有一个名为getWeight(left, right)的公共方法，该方法接收两个索引数组，并根据在所
传递的索引处发现的数值的累加，返回-1、0或1，这些数值是较重、相等或较轻的。

getWeight返回。如果左盘较重则返回-1
如果右锅较重，则返回1.如果两个平底锅的重量相同，则返回0
scales.getWeight()的用法示例。

scales.getWeight([3], [7]) 如果球3比球7重，则返回-1；如果球7更重，则返回1；
果这些球的重量相同，则返回0。

scales.getWeight([3, 4], [5, 2]) 如果球3和4的重量比球5和2的重量重，返回-1。

那么，你可能会问，问题出在哪里呢？嗯--这个天平很老了。在天平损坏之前，你只能使用它3次。

太容易了？太难了？试试其他级别。

有8个球，编号从0到7，其中7个球的重量相同。有一个比较重。你的任务是找出它的号码。
你的函数findBall将收到一个参数--scales对象。天平对象包含一个内部存储的8个元素
的数组（索引为0-7），每个元素都有相同的值，只有一个元素更大。

它还有一个名为getWeight(left, right)的公共方法，该方法接收两个索引数组，并根
据在所传递的索引处发现的数值的累加，返回-1、0或1，这些数值是较重、相等或较轻的。

getWeight返回。

如果左盘较重则返回-1
如果右锅较重，则返回1
如果两个平底锅的重量相同，则返回0
scales.getWeight()的用法示例。
scales.getWeight([3], [7])
如果球3比球7重，则返回-1；
如果球7更重，则返回1；如果这些球的重量相同，则返回0。

scales.getWeight([3, 4], [5, 2]) 如果球3和4的重量比球5和2的重量重，返回-1。

那么，你可能会问，问题出在哪里呢？嗯--这个天平很老了。在天平损坏之前，你只能使用它3次。


def find_ball(scales):
    # call scales.get_weight() at most 3 TIMES
    # return indexOfHeavierBall
    for i in range(1, 8):
        leftPan = [i-1]
        rightPan = [i]
        w = scales.get_weight(leftPan, rightPan)

        if w < 0:
            return leftPan[0]

        if w > 0:
            return rightPan[0]


'''

def find_ball(scales):
    balls = [0, 1, 2, 3, 4, 5, 6, 7]

    while len(balls) > 1:
        l, r = balls[:len(balls) // 2], balls[len(balls) // 2:]
        w = scales.get_weight(l, r)
        balls = l if w < 0 else r
    return balls[0]



def find_ball(scales):
    # call scales.get_weight() at most 3 TIMES
    # return indexOfHeavierBall
    leftPan = scales[:len(scales)//2]
    rightPan = scales[len(scales)//2:]
    while leftPan != rightPan:
        w = scales.get_weight(leftPan, rightPan)
        if w < 0:
            leftPan = rightPan[:len(rightPan)//2]
            rightPan = rightPan[len(rightPan)//2:]
        if w > 0:
            leftPan = leftPan[:len(rightPan) // 2]
            rightPan =leftPan[len(rightPan) // 2:]
    return max(leftPan,rightPan)

