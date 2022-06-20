'''
https://brilliant.org/practice/computer-science-warmups-level-2-challenges/?p=3

计算机科学热身赛。第二级挑战
再试一次

Sandip、Tracy、Jamal和Sheng是最好的朋友，他们每天一起在香蕉摊工作。
由于他们关系密切，他们在任何一天的幸福感都取决于其他三个人在前一天的幸福感。
假设他们的行为如下。

如果昨天特蕾西和贾马尔都很开心的话 阿胜今天才会开心。
只有在昨天Sandip或Sheng（或两个人）都快乐的情况下，Jamal今天才会快乐。
Sandip喜欢看Sheng哭，所以只有当Sheng昨天伤心时，Sandip今天才会开心。
Tracy只有在Tracy昨天开心的情况下，今天才会开心，也就是说她有独立的倾向。


假设第一天，四个朋友都很伤心。几天后，朋友们的情绪状态达到稳定，重复出现。
在这种重复状态下，每个人的情绪状态是什么？


if Tracy == 1 and Jamal == 1:
    sheng = 1

if Sandip == 1 or Sheng == 1:
    Jamal = 1

if Sheng == 0:
    Sandip = 1

if Tracy == 1:
    Tracy = 1

'''

Sandip,Tracy,Jamal,Sheng = 0,0,0,0

day = 10
motion = [Sandip,Tracy,Jamal,Sheng]
def repeat_motion(day,Sandip,Tracy,Jamal,Sheng):
    d = 0
    res = []
    while d < day:
        print(Sandip,Tracy,Jamal,Sheng)
        if Tracy == 1 and Jamal == 1:
            Sheng = 1

        if Sandip == 1 or Sheng == 1:
            Jamal = 1

        if Sheng == 0:
            Sandip = 1

        if Tracy == 1:
            Tracy = 1

        res.append([Sandip,Tracy,Jamal,Sheng])
        d += 1
    return res

print(repeat_motion(day,Sandip,Tracy,Jamal,Sheng))

# Brilliant post
sandip_y = False
sheng_y = False
jamal_y = False
tracy_y = False
while True:
    sandip = not sheng_y
    sheng = tracy_y and jamal_y
    jamal = sandip_y or sheng_y
    tracy = tracy_y
    if (sandip,sheng,jamal,tracy)==(sandip_y,sheng_y,jamal_y,tracy_y):
        break
    sandip_y,sheng_y,jamal_y,tracy_y = sandip,sheng,jamal,tracy
print("Sandip:", sandip)
print("Sheng:", sheng)
print("Jamal:", jamal)
print("Tracy:", tracy)


'''

1. dog狗2. cat猫3. panda熊猫4. elephant大象5. tiger老虎
6. lion狮子7. monkey猴子8. gorilla大猩猩9. glede老鹰
10. kangaroo袋鼠11. koala考拉12. dolphin海豚
13. snake蛇14. goldfish金鱼  15. shark鲨鱼.16. duck鸭
17. chicken鸡18. cow母牛19. cattle牛20. sheep羊
21. goose鹅22. horse马23. wolf狼24. fish鱼25. bird鸟
26. pig猪，27 松鼠：Squirrel
计算机科学热身赛第二级挑战
天敌相遇吗

在野生动物园有Squirrel、Turtle、fox和Snake四种动物之间存在天敌或者朋友的关系，
它们每天观察其他三只动物,再决定是否走出自己的安全小窝。假如他们的行为如下。

Squirrel、fox都出来了，Snake才会出来！
Squirrel，Snake中的某一只出来，或Squirrel和Snake都出来的情况下，fox才会出来！
Squirrel看到Snake没有出来时，Squirrel才会出来
Turtle很佛系，Turtle不关心其他三只动物的状态，Turtle保持前一天的状态

假设第一天，四只动物都在窝里。预测若干天以后各自的状态是什么？
并且试着找到规律
'''
Squirrel,Turtle,fox,Snake= 0,0,0,0

day = 10
#motion = [Squirrel,Turtle,fox,Snake]
def repeat_motion(day,Squirrel,Turtle,fox,Snake):
    d,same = 1,True
    status = [(0,0,0,0)] #第一天初始状态

    while same:
        d += 1
        print(Squirrel,Turtle,fox,Snake)
        if Turtle == 1 and fox == 1:
            snake = 1

        if Squirrel == 1 or Snake == 1:
            fox = 1

        if Snake == 0:
            Squirrel = 1

        Turtle = Turtle

        print(d,list(zip((Squirrel,Turtle,fox,Snake),status[-1])))
        same = any(x!=y for x,y in list(zip((Squirrel,Turtle,fox,Snake),status[-1])))
        #判断前后两天的状态是否相同
        if same:
            status.append([Squirrel,Turtle,fox,Snake])
        else:return d,status[-1]

print("Squirrel,Turtle,fox,Snake")
print(repeat_motion(day,Squirrel,Turtle,fox,Snake))

# day=1时，Squirrel,Turtle,fox,Snake都在窝里=False
Squirrel_1 = False
Turtle_1 = False
fox_1 = False
Snake_1 = False
day = 1

while True:
    day += 1
    Squirrel = not Snake_1
    Snake = Turtle_1 and fox_1
    fox = Squirrel_1 or Snake_1
    Turtle = Turtle_1
    print(day)
    if (Squirrel,Turtle,fox,Snake)==(Squirrel_1,Turtle_1,fox_1,Snake_1):
        break
    Squirrel_1,Turtle_1,fox_1,Snake_1 = Squirrel,Turtle,fox,Snake

print(f'第{day}天后，动物都稳定在下述状态：')
print("Squirrel:", Squirrel)
print("Turtle:", Turtle)
print("fox:", fox)
print("Snake:", Snake)




'''

计算机科学热身赛第二级挑战
再试一次

有ada,bob,cindy,dior四个同学在各自宿舍玩灯光游戏：
Sandip、Tracy、Jamal和Sheng是最好的朋友，他们每天一起在香蕉摊工作。
由于他们关系密切，他们在任何一天的幸福感都取决于其他三个人在前一天的幸福感。
假设他们的行为如下。

如果bob和cindy两人的宿舍灯亮了，那么今天才会开心。
只有在昨天Sandip或Sheng（或两个人）都快乐的情况下，Jamal今天才会快乐。
Sandip喜欢看Sheng哭，所以只有当Sheng昨天伤心时，Sandip今天才会开心。
Tracy只有在Tracy昨天开心的情况下，今天才会开心，也就是说她有独立的倾向。


假设第一天，四个朋友都很伤心。几天后，朋友们的情绪状态达到稳定，重复出现。
在这种重复状态下，每个人的情绪状态是什么？
'''

