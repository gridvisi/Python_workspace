'''
https://www.codewars.com/kata/55192f4ecd82ff826900089e/train/python
天气太热了，他们甚至不能...
一个炎热的夏天，皮特和他的朋友比利决定去买西瓜。他们选择了最大的一箱。他们赶回家，
快渴死了，决定把他们的战利品分掉，然而他们面临一个难题。

皮特和比利是偶数的忠实粉丝，这就是为什么他们想把西瓜的数量分成两部分，使每一部分
都由偶数的西瓜组成。然而，这并不意味着这两部分必须相等。

例如：男孩们可以把一叠8个西瓜分成2+6个瓜，或4+4个瓜。

孩子们非常累，想尽快开始吃饭，所以你应该帮助他们，看看他们是否能按自己的方式来分
水果。可以肯定的是，他们每个人都应该得到正数的一部分。

任务
给出一个西瓜的整数w（1≤w≤100；在Haskell中为1≤w），检查Pete和Billy是否能将
西瓜分成两份，使他们每个人得到的数量相等。

例子
test.assert_equals(divide(4), True)
        test.assert_equals(divide(2), False)
        test.assert_equals(divide(5), False)
        test.assert_equals(divide(88), True)
        test.assert_equals(divide(100), True)
        test.assert_equals(divide(67), False)
        test.assert_equals(divide(90), True)
        test.assert_equals(divide(10), True)
        test.assert_equals(divide(99), False)
        test.assert_equals(divide(32), True)
'''


def divide(weight):
    return weight > 2 and weight % 2 == 0

def divide(weight):
    return weight%2 == 0 if weight > 2 else False