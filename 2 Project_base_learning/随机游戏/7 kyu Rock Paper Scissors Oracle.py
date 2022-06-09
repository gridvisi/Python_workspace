'''
https://www.codewars.com/kata/580535462e7b330bd300003d/train/python

你是石头剪子布的神谕。

闻名于世，你有惊人的能力预测你的对手会从石头、纸和剪刀中选择哪种手势。

不幸的是，你不再是个年轻人了，在两轮比赛之间，你的手难以移动。出于这个原因，你只能为每个对手选择一个手势。如果你有可能获胜，你会的，但你也很乐意打平。

给出一个手势数组--例如["纸"、"剪刀"、"剪子"]--按照它们在标题中出现的顺序返回获胜的手势，中间用正斜线分开。例如，如果石头和剪刀都可以用来取胜，你将返回。

"石头/剪子"

如果你不可能获胜，则返回。

"平局"

如果你不熟悉 "石头剪刀布"，请看https://en.wikipedia.org/wiki/Rock%E2%80%93paper%E2%80%93scissors。

我的第一个卡塔的第二次尝试...

from solution import oracle

@test.describe("Fixed Tests")
def fixed_test_cases():
    @test.it("Example Tests")
    def example_test_cases():
        test.assert_equals(oracle(["rock","paper","scissors","rock"]), "paper")
        test.assert_equals(oracle(["rock","paper","scissors"]), "tie")
        test.assert_equals(oracle(["rock","paper","paper","scissors","scissors"]), "scissors")
        test.assert_equals(oracle(["paper","scissors","scissors"]), "rock/scissors")
'''

# ericlee solution
def oracle(gestures):
    ans = dict(zip(["rock", "paper", "scissors"], [0, 0, 0]))
    gaming = {'rp': -1, 'pr': 1, 'ps': -1, 'sp': 1, 'sr': -1, 'rs': 1}
    for k, v in ans.items():
        for g in gestures:
            ans[k] += gaming.get(k[0] + g[0], 0)
    if len(set(ans.values())) == 1: return 'tie'
    return '/'.join([k for k, v in ans.items() if v > 0])


def oracle(gestures):
    ans = dict(zip(["rock","paper","scissors"],[0,0,0]))
    gaming = {'rp':-1,'pr':1,'ps':-1,'sp':1,'sr':-1,'rs':1}
    for k,v in ans.items():
        for g in gestures:
            print(k[0]+g[0],gaming.get(k[0]+g[0],0))
            ans[k] += gaming.get(k[0]+g[0],0)
    if len(set(ans.values())) == 1:return 'tie'
    return '/'.join([k for k,v in ans.items() if v == max(ans.values())])

gestures = ["rock","paper","scissors","rock"]
gestures = ["rock","paper","paper","scissors","scissors"]
gestures = ["paper","scissors","scissors"]
gestures = ["rock","paper","scissors"]
gestures = ["rock","paper","scissors","paper","paper","scissors","scissors","scissors","scissors"]
print(oracle(gestures))

#max(Counter([winGest[i] for i in gestures]),key=lambda x:winGest.values)
#work your magic here
#winGest = dict(zip(["rock","paper","scissors"],["paper","scissors","rock"]))


#1st
from collections import Counter

def oracle(gestures):
    res, C = [], Counter(gestures)
    if C["scissors"] > C["paper"]:    res.append("rock")
    if C["rock"]     > C["scissors"]: res.append("paper")
    if C["paper"]    > C["rock"]:     res.append("scissors")
    return "/".join(res) or "tie"