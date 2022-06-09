'''
https://www.codewars.com/kata/greed-is-good/train/python
Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point
 A single die can only be counted once in each roll. For example, a "5" can only count as part of a triplet (contributing to the 500 points) or as a single 50 points, but not both in the same roll.
Example scoring

 Throw       Score
 ---------   ------------------
 5 1 3 4 1   50 + 2 * 100 = 250
 1 1 1 3 1   1000 + 100 = 1100
 2 4 4 5 4   400 + 50 = 450
'''
dict_rule = {'111':1000,'666':600,'555':500,'444':400,'333':300,'222':200,'1':100,'5':50}
dice = [5,1, 3, 4, 1 ]
print(''.join([str(i) for i in sorted(dice)]))
def score(dice):
    point,re = 0,[]
    for k,v in dict_rule.items():
        re.append(k)
        if k in ''.join([str(i) for i in sorted(dice)]):
            point += dict_rule[k]
            print(re)
            return dict_rule[k],re

print(score(dice))

'''
        re = filter(lambda x:i,[i for i in dice])
        return list(re)
'''