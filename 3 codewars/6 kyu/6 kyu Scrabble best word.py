'''
https://www.codewars.com/kata/563f960e3c73813942000015/train/python
'''
words = ["WHO","IS","THE","BEST","OF","US","WBC","XY","XJD"] #0
points = (1,3,3,2,1,4,2,4,1,8,10,1,2,1,1,3,8,1,1,1,1,4,10,10,10,10)
import string
s = string.ascii_letters
print(s[26:])
def get_best_word(points, words):
    re = {}#[0]*len(words)
    point_dic = dict(zip(s[26:],points))
    for i,w in enumerate(words):
        re[w] = sum([point_dic[i] for i in w])

    max_v = max([v for k,v in re.items()])
    res = [(len(k),k,v) for k,v in re.items() if re[k] == max_v]
    #print(res)
    return words.index(sorted(res)[0][1])


#Top 1st solution
from string import ascii_uppercase as uppercase
def get_best_word(points, words):
    points = dict(zip(uppercase, points))
    score = lambda word: sum(points[c] for c in word)
    print("score:")
    return words.index(sorted(sorted(words, key=len), key=score, reverse=True)[0])
print(get_best_word(points, words))

def get_best_word(points, words):
    score = { i:sum( points[ord(x)-65] for x in e ) for i,e in enumerate(words)  }
    return min( [e[0] for e in score.items() if e[1] == max(score.values()) ], key = lambda x: len( words[x]) )
