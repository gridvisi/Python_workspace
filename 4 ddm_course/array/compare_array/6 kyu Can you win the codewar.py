'''
https://www.codewars.com/kata/5e3f043faf934e0024a941d7/train/python

两个王国正在交战，由于你的法典战士的威力，你被交战国之一任命为将军。你的对手的军队比你的大，但如果你是一个优秀的战略家，也许你可以达成僵局，甚至赢得冲突。

你控制的军队数量与对手国家的军队数量相同，但他们的军队一般更大。你必须派出一支军队来对抗对手的每一支军队。
这意味着会有和军队一样多的战斗）。
没有可能出现大卫和巨人的意外：战斗的结果总是大军的胜利（如果双方规模相同，则是对峙）。
胜利的一方是赢得最多战役的一方。
如果双方胜仗次数相同，结果可能是僵持。

你必须写一个函数

codewar_result(codewarrior, opponent)
输入双方的军队，用严格的正整数数组来表示他们的规模。该函数根据你方的战争结果返回字符串 "失败"、"僵持 "或 "胜利"，并为你方提供最佳策略。

例如，如果你有3支军队，规模为[1,4,1]，而对手的军队规模为[1,5,3]，尽管你的平均兵力较少，但仍有可能达成僵局。

1-1 : 僵持
4-3：你的胜利
1-5：对方军队的胜利
尘埃落定，一荣俱荣，一损俱损，优柔寡断。

codewar_result([1，4，1]，[1，5，3])
应该返回 "Stalemate"。

更多例子:
codewar_result([2, 4, 3, 1], [4, 5, 1, 2])
应该返回 "胜利"，因为这样处置你的军队是有可能获胜的 。

2-1
4-4
3-2
1-5
从而赢得两场战斗，死守一场，输掉一场。

codewar_result([1，2，2，1]，[3，1，2，3])
应该返回 "失败"，因为即使有一个最佳的策略，也不可能赢。你能做的最好的是一胜一平 。

@test.describe('Sample Tests')
def sample_tests():
    test.assert_equals(codewar_result([1, 4, 1], [1, 5, 3]), 'Stalemate')
    test.assert_equals(codewar_result([2, 4, 3, 1], [4, 5, 1, 2]), 'Victory')
    test.assert_equals(codewar_result([1, 2, 2, 1], [3, 1, 2, 3]), 'Defeat')
    test.assert_equals(codewar_result([1, 1, 1, 1], [1, 1, 1, 1]), 'Stalemate')
    test.assert_equals(codewar_result([5], [6]), 'Defeat')
    test.assert_equals(codewar_result([2, 1, 3, 1, 1, 3, 3, 2, 3, 1, 1, 1, 3, 1, 3, 1, 3, 3, 1, 2, 3, 3, 1, 3],
    [4, 4, 1, 4, 3, 1, 4, 4, 3, 2, 1, 2, 1, 3, 3, 1, 4, 4, 3, 2, 3, 2, 4, 1]), 'Stalemate')
'''


def codewar_result (codewarrior, opponent):
    #our,opp = sorted(codewarrior),sorted(opponent)

    print(our,opp)
    pk = [0 if x==y else (x-y)//abs(x-y) for x, y in zip(our, opp)]
    print(pk)
    if sum(pk) == 0:return 'Stalemate'
    elif sum(pk) < 0:return 'Defeat'
    elif sum(pk) > 0:return 'Victory'
codewarrior, opponent = [1, 4, 1], [1, 5, 3]
print(codewar_result (codewarrior, opponent))