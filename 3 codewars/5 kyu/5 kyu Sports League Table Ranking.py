'''

https://www.codewars.com/kata/sports-league-table-ranking/train/python
注：有一个更难的版本（体育联赛排名（与头对头））这一点。说明
你以循环制组织一个体育联盟。每个队都会遇到其他队。在你的联赛中，一场胜利给一个队2分，一场平局给两个队1分。几场比赛后，你必须计
算出你所在联盟球队的顺序。您可以使用以下条件来安排团队：点数得分差距（得分和失球的差距）
进球数首先你要按分数给各队排序。如果两个或多个队达到相同的分数，则第二个标准开始发挥作用，以此类推。最后，如果所有标准都相同，
那么团队共享一个位置。
输入
数量：你所在联盟的球队数量。
游戏：数组。每一个项目代表一个由四个元素组成的游戏数组【TeamA，TeamB，GoalA，GoalB】（TeamA与TeamB比赛，进球和失球）。
输出
位置：一系列的位置。第i项应该是你们联盟第i队的位置。
例子
'''
number = 6
games = [[0, 5, 2, 2],   #// Team 0 - Team 5 => 2:2
         [1, 4, 0, 2],   #// Team 1 - Team 4 => 0:2
         [2, 3, 1, 2],   #// Team 2 - Team 3 => 1:2
         [1, 5, 2, 2],   #// Team 1 - Team 5 => 2:2
         [2, 0, 1, 1],   #// Team 2 - Team 0 => 1:1
         [3, 4, 1, 1],   #// Team 3 - Team 4 => 1:1
         [2, 5, 0, 2],   #// Team 2 - Team 5 => 0:2
         [3, 1, 1, 1],   #// Team 3 - Team 1 => 1:1
         [4, 0, 2, 0]]   #// Team 4 - Team 0 => 2:0

'''
You may compute the following table:
Rank	Team	For : Against	GD	Points
1.	Team 4	5 : 1	+4	5
2.	Team 5	6 : 4	+2	4
3.	Team 3	4 : 3	+1	4
4.	Team 0	3 : 5	-2	2
4.	Team 1	3 : 5	-2	2
6.	Team 2	2 : 5	-3	1
Team 5 and Team 3 reached the same number of points. But since Team 5 got a better scoring differential, it ranks better than Team 3. All values of Team 0 and Team 1 are the same, so these teams share the fourth place.
In this example you have to return the array [4, 4, 6, 3, 1, 2].
'''

def compute_ranks(number, games):
    team,score = [0]* number,[0]*number
    print(team)
    for c in games:
        score[c[0]] += c[2] - c[3]
        score[c[1]] += -c[2] + c[3]

        if c[2] > c[3]:
            team[c[0]] += 2

        elif c[2] == c[3]:
            team[c[0]] += 1
            team[c[1]] += 1
        if c[2] < c[3]:
            team[c[1]] += 2
    total = [team[i] + score[i] for i in range(len(team))]
    rank = sorted(total,reverse=True)
    res = [rank.index(i)+1 for i in total]
    return  res,team,score,total,
# rank [4, 4, 6, 3, 1, 2]
print(compute_ranks(number, games))
number = 6
games=          [[0, 5, 2, 0],  #0队 2分 5队 0分
                 [1, 4, 2, 2],  #1队 1分 4队 1分
                 [2, 3, 1, 3],  #2队 0分 3队 2分
                 [1, 5, 0, 0],  #1队 1分 5队 1分
                 [2, 0, 2, 1],  #2队 2分 0队 0分
                 [3, 4, 3, 1]]  #3队 2分 4队 0分

'''
You may compute the following table:
Rank Team	For :   Against	GD	Points
1.	Team 3	6 : 2	+3	4+4    赢2场
2.	Team 0	3 : 2	+1	1+2    赢1场，输1场
3.	Team 1	2 : 2	0	0+2    平2场
4.	Team 2	3 : 4	-1	2-1    赢1场，输1场
4.	Team 4	3 : 5	-2	1-2    平1场，输1场
6.	Team 5	0 : 2	-2	1-2    平1场，输1场
'''
# [2,3,4,1,5,6])
print(compute_ranks(number, games))


'''

def compute_ranks(number, games):
    team,score = [0]* number,[0]*number
    print(team)
    for c in games:
        score[c[0]] += c[2]
        score[c[1]] += c[3]
        if c[2] > c[3]:
            team[c[0]] += 3

        elif c[2] == c[3]:
            team[c[0]] += 1
            team[c[1]] += 1
        if c[2] < c[3]:
            team[c[1]] += 3
    total = [team[i] + score[i] for i in range(len(team))]
    rank = sorted(total,reverse=True)
    res = [rank.index(i)+1 for i in total]
    return  res,team,score,total,
# rank [4, 4, 6, 3, 1, 2]

'''

def compute_ranks(number, games):
    table = [[team] for team in range(number)]
    for team in table:
        for _ in range(0,4):
            team.insert(0, 0)
    for match in games:
        t1, t2, s1, s2 = match[0:4]
        table[t1][2] += s1
        table[t1][3] += s2
        table[t2][2] += s2
        table[t2][3] += s1
        if s1 > s2:
            table[t1][0] += 2
        elif s2 > s1:
            table[t2][0] += 2
        else:
            table[t1][0] += 1
            table[t2][0] += 1
    for team in table:
        team[1] = team[2] - team[3]
    table.sort(reverse=True)
    print (table)
    ranking = [0 for _ in range(0,number)]
    for place, team in enumerate(table):
        if place > 0 and team[0] == table[place - 1][0] and team[1] == table[place - 1][1] and team[2] == table[place - 1][2]:
            ranking[team[4]] = ranking[table[place - 1][4]]
        else:
            ranking[team[4]] = place + 1
    return ranking

print(compute_ranks(number, games))