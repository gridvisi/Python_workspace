

string = 'Arsenal just conceded another goal, two nil'
num = [str(i) for i in range(10)]
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
num = [0 ,1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9]
#print(num)
scr = ['nil','one','two','three','four','five','six','seven','eight','nine']
dic = dict(zip(scr,num))

print(dic)

string = "new score: two three"
def scoreboard(string):
    scr = ['nil', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    res,dic  = [],dict(zip(scr,num))
    for w in string.split(' '):
        if w in scr:
            res.append(dic[w])
    return res

def scoreboard(string):
    scores = {'nil': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    return [scores[x] for x in string.split() if x in scores]
print(scoreboard(string))