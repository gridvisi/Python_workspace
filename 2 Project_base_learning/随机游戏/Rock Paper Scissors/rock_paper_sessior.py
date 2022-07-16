
s = {'1',1,1,'1','0',0,0,1}
print(len(set(s)),set(s)) #去重复的元素


p1, p2 = "scissors", "paper"
p1, p2 = p2, p1
#print(p1,p2)
def rps(p1, p2):
    key = p1[0] + p2[0]
    #if p1[0] == p2[0]:return 'Draw!'
    print(set(list(key)))
    if len(set(list(key))) == 1:
        return 'Draw!'
    rules = {
            'sp':'win',
             'rs':'win',
             'pr':'win'
             }
    print('判断是否包含某个keys值：','sp' in rules)
    res = f"player 1 {rules.get(key,'LOSE')}"
    return res

    #DICT 字典写入一个[key]
p1, p2 = "scissors", "paper"
#p1, p2 = "rock", "paper"
#p1, p2 = "scissors", "rock"
#p1, p2 = "scissors", "scissors"
print('result:',rps(p1,p2))

def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"

def rps(p1, p2):
    hand = {'rock':0, 'paper':1, 'scissors':2}
    results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
    return results[hand[p1] - hand[p2]]
