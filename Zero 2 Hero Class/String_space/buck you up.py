'''
Input:
s1 = “I've got the fuck money,so fuck you!"
s2 = "I want my job back,you can fuck me if you want"

Output:
"You've got the buck money, so buck you up!"
"You want your job back, you can buck you up if you want"

红色部分就是输入和输出变化的部分。输入和输出的变化归纳为：
I  -> You
my -> your
fuck -> buck
'''

def replace(prev,repl,s1,s2):
    s = s1 + ' ' + s2
    rep_dict = dict(zip(prev,repl))
    for w in prev:
        s.replace(w, rep_dict[w])
    return s

#[s.replace(w,rep_dict[w]) for w in prev]

def replace(prev,repl,s1,s2):
    s = s1 + ' ' + s2
    rep_dict = dict(zip(prev,repl))
    for w in prev:
        s.replace(w, rep_dict[w])
    return s
prev,repl = ['I','my','your'],['You','your','buck']
s1 = "You've got the buck money, so buck you up!"
s2 = "You want your job back, you can buck you up if you want"
print(replace(prev,repl,s1,s2))

'''
My dear Dad, I may find my man in future who will love me from his heart and soul but I am sure 
that I cannot find a man who can stand even near to your love for me! You are the best, today, 
tomorrow and always!!

我亲爱的爸爸，也许我将来会找到我的男人，他会发自内心地爱我，但我相信，我找不到一个男人能和你对我的爱相提并论! 您是最好的，今天，明天，永远都是最好的!!!

第二个任务是找到上面句子中每一个love后面紧跟的单词​
'''

s = '''My dear Dad, I may find my man in future who will love me from his heart and soul but I am sure
that I cannot find a man who can stand even near to your love for me! You are the best, today, 
tomorrow and always!!'''
print(s)

def love_obj(s):
    return [w.split(" ")[0] for w in s.split('love ')[1:]] #[w for w in s.split(' ') if w == 'love']
print(love_obj(s))

quots = '''
4 years: My Daddy can do anything!
7 years: My Dad knows a lot…a whole lot.
8 years: My father does not know quite everything.
12 years: Oh well, naturally Father does not know that either.
14 years: Oh, Father? He is hopelessly old-fashioned.
21 years: Oh, that man-he is out of date!
25 years: He knows a little bit about it, but not much.
30 years: I must find out what Dad thinks about it.
35 years: Before we decide, we will get Dad's idea first.
50 years: What would Dad have thought about that?
60 years: My Dad knew literally everything!
65 years: I wish I could talk it over with Dad once more
'''

def fatherday(quots):
    arr = []
    st = quots.split('years:')
    st = [w.split('\n') for w in st]
    for i,e in enumerate(st[:-1]):
        arr.append([e[1],st[i+1][0]])
    return dict(arr)
print(fatherday(quots))
