
'''
在晨练中，你要求你的士兵排成五排。您注意到最后一排有三名士兵。
然后你让它们以八个为一组重新形成，最后一行留下七个，然后是九个行，
留下两个。你从来没有计算过你所有的士兵，但现在你有足够的信息来确
定总数，而不必明确说明。​避免泄露给敌人可以拦截的士兵数量。
'''


ans = []
for n in range(200):
    if n%5==3 and n%8==7 and n%9==2:
        ans.append(n)
print(ans)


ans = []
total = 1000
for n in range(total):
    if n%5==3 and n%8==7 and n%9==2:
        ans.append(n)
print(ans)
