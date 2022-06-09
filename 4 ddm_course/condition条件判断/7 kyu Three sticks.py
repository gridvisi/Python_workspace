'''

https://www.codewars.com/kata/57c1f22d8fbb9fd88700009b/train/python
想象一下，给你两根棍子，你想最终得到三根长度相等的棍子。你想最终得到三根长度相等的棍子。为了达到这个目的，
你可以将其中一根或两根棍子剪断，也可以将剩余的部分扔掉。

写一个函数 maxlen，取两根小棒的长度（L1 和 L2，都是正值），返回你能做的三根小棒的最大长度。
'''

def maxlen(L1,L2):
    s,l = min(L1,L2),max(L1,L2)
    if l//2 >= s:return s
    else:return int(s//2)+1


def maxlen(s1, s2):
    sm, lg = sorted((s1, s2))
    return min(max(lg / 3, sm), lg / 2)