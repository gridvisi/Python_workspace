'''
你是石头剪子布的神谕。

闻名于世，你有惊人的能力预测你的对手会在石头、纸和剪刀中选择哪种手势。

不幸的是，你不再是个年轻人了，在两轮比赛之间，你的手难以移动。出于这个原因，
你只能为每个对手选择一个手势。如果你有可能获胜，你会的，但你也很乐意打平。

给出一个手势数组--例如["纸"、"剪刀"、"剪子"]--按照它们在标题中出现的顺序
返回获胜的手势，中间用正斜线分开。例如，如果石头和剪刀都可以用来取胜，你会返回。

"石头/剪子"

如果你不可能获胜，则返回。

 g = ["rock","paper","scissors"]
'''
from collections import Counter

def oracle(gestures):
    #work your magic here
    cunt = Counter(gestures)
    return cunt

gestures = ["rock","paper","paper","scissors","scissors"]
print(oracle(gestures))