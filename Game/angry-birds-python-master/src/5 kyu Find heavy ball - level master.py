'''
描述。
有8个球，编号从0到7，其中7个球的重量相同。有一个更重。你的任务是找到它的号码。

你的函数findBall将收到一个参数--scales对象。天平对象包含一个内部存储的8个元素的数组（索引为0-7），
每个元素都有相同的值，只有一个元素更大。它还有一个名为getWeight(left, right)的公共方法，
该方法接收两个索引数组，并根据在所传递的索引处发现的数值的累加，返回-1、0或1，这些数值是较重、相等或较轻的。

getWeight返回。

如果左盘较重则返回-1

如果右锅较重，则返回1

如果两个平底锅的重量相同，则返回0

scales.getWeight()的用法示例。

scales.getWeight([3], [7]) 如果球3比球7重，则返回-1；如果球7更重，则返回1；如果这些球的重量相同，则返回0。

scales.getWeight([3, 4], [5, 2]) 如果球3和4的重量比球5和2的重量重，返回-1。

那么，你可能会问，问题出在哪里呢？好吧--这个天平非常古老。在天平损坏之前，你只能使用它两次。

注意 - 在Python、Crystal和Ruby版本中使用scales.get_weight()。

太难了？试试更低的级别。

新手
征服者
还是太容易？试试这个卡塔 - ubermaster (由bellmyer制作)
'''

def find_ball(scales):
    part = [[None, 0, 1], [2, 3, 4], [5, 6, 7]]
    res1 = scales.get_weight(part[-1], part[1])
    res2 = scales.get_weight([part[res1][-1]], [part[res1][1]])
    return part[res1][res2]