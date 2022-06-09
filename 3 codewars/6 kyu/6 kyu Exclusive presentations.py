#https://www.codewars.com/kata/57dd8c78eb0537722f0006bd/train/python
'''
A group of friends (n >= 2) have reunited for a get-together after a very long time.
They agree that they will make presentations on holiday destinations or expeditions they have been to only if it satisfies one simple rule:
the holiday/journey being presented must have been visited only by the presenter and no one else from the audience.
Write a program to output the presentation agenda, including the presenter and their respective presentation titles.

他们一致认为，只有在满足一个简单的规则的情况下，他们才会对他们去过的度假地或探险活动进行介绍。
所介绍的假期/旅程必须只有介绍人去过，而没有其他听众。
编写一个程序来输出演讲议程，包括演讲者和他们各自的演讲题目。
'''
friend_list = [
    {'person': 'Abe', 'dest': ['London', 'Dubai']},
    {'person': 'Bond', 'dest': ['Melbourne', 'Dubai']},
    {'person': 'Carrie', 'dest': ['Melbourne']},
    {'person': 'Damu', 'dest': ['Melbourne', 'Dubai', 'Paris']}
    ]
#[{'person': 'Abe',  'dest': ['London']}, {'person': 'Damu', 'dest': ['Paris']}]

def presentation_agenda(friend_list):
    pd = ' '.join([' '.join(p['dest']) for p in friend_list])
    res = [i for i in pd.split(' ') if pd.split(' ').count(i) == 1]
    ans = []
    for i in friend_list:
        if set(res) & set(i['dest']):
            i['dest'] = sorted([i for i in set(res) & set(i['dest'])])
            ans.append(i)
    return ans
print(presentation_agenda(friend_list))

from collections import Counter

def presentation_agenda(friend_list):
    uniqueDest    = {d for d,c in Counter(d for p in friend_list for d in p['dest']).items() if c == 1}
    pFilteredDest = tuple((p['person'], [d for d in p['dest'] if d in uniqueDest]) for p in friend_list)
    return [{'person': name, 'dest': lst} for name,lst in pFilteredDest if lst]

def presentation_agenda(friend_list):
    out = []
    for friend in friend_list:
        p_list = friend['dest']
        for f in friend_list:
            p_list = [loc for loc in p_list if f == friend or loc not in f['dest']]
        if len(p_list):
            out.append({'person': friend['person'], 'dest': p_list})
    return out

'''
def presentation_agenda(friend_list):
    pd = ' '.join([' '.join(p['dest']) for p in friend_list])
    res = [i for i in pd.split(' ') if pd.split(' ').count(i) == 1]
    for p in friend_list:
        ans = [k for k,v in p.items() if v
    return res
'''