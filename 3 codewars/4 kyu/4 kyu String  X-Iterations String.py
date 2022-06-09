'''
https://www.codewars.com/kata/string->-x-iterations->-string/train/python
example where s = "String" and x = 3:

after 0 iteration  s = "String"
after 1 iteration  s = "gSntir"
after 2 iterations s = "rgiStn"
after 3 iterations s = "nrtgSi"

so you would return "nrtgSi".Let's say you start with this: "String"
假设你从这个开始：“字符串”
The first thing you do is reverse it: "gnirtS"
你要做的第一件事就是把它颠倒过来：“gnirtS”
Then you will take the string from the 1st position and reverse it again: "gStrin"
然后从第一个位置取下字符串并再次反转：“gStrin”
Then you will take the string from the 2nd position and reverse it again: "gSnirt"
然后从第二个位置取下绳子，再将其反转：“gSnirt”
Then you will take the string from the 3rd position and reverse it again: "gSntri"
然后从第三个位置取下字符串并再次反转：“gSntri”
Continue this pattern until you have done every single position, and then you will return the string you have created. For this particular string, you would return: "gSntir"
继续此模式，直到完成每个位置，然后返回创建的字符串。对于这个字符串，您将返回：“gSntir”

s,x = "String",3
print([i for i in range(len(s)) if i % 2 == 0][::-1])
ls = list("String")
ls.insert(0,'x')
list("String").insert(0,'x')
print(ls)
'''

s,x = "String for test：incommensurability",1
#"ySttirliinbga rfuosrn etmemsotc:n i"
#s,x = "Ohh Man God Damn",7   #" nGOnmohaadhMD  "

s,x = "Ohh Man God Damn",7  #nGOnmohaadhMD  "
s,x = "String",3  #"nrtgSi"

a = ["s"]
a.insert(0,'g')
print(a)

def flip(s):  #"gSntir"
    ls,i = list(s),0
    front, tail = [],ls
    print('mark:', front, tail)
    while i < len(s):
        front,tail = front+[tail[-1]],tail[:len(s)-i-1]
        re,tail = front + tail[::-1],tail[::-1]
        print(re, front, tail)
        i += 1
    return ''.join(re)
s = "String"
print('flip',flip(s))

def func(s,x):
    if x > 0:
        s = flip(s)
        x -= 1
        return func(s,x)
    elif x == 0:return ''.join(s)


def flip(s):
    front, tail = [], list(s)
    for i in range(len(s)):
        front, tail = front + [tail[-1]], tail[:len(s) - i - 1]
        re, tail = front + tail[::-1], tail[::-1]

    return ''.join(re)


def func(s, x):
    if x > 0:
        s = flip(s)
        x -= 1
        return func(s, x)
    elif x == 0:
        return ''.join(s)

s,x = "Ohh Man God Damn",7
print('final:',func(s,x))

'''

        front, tail = s[:i + 1], s[i + 1:]
        front,tail = tail[-1]+front,tail[:-1][::-1]
        print(front,tail)
        s = front + tail
        print('s:',s)
        
        
after 0 iteration  s = "String"
after 1 iteration  s = "gSntir"
after 2 iterations s = "rgiStn"
after 3 iterations s = "nrtgSi"

def func(s,x): # pycharm 正确执行，but not valid for codewars
    slf = [0] * len(s)
    for i in range(len(s) // 2):
        # print(len(s) // 2, slf)
        slf[2 * i] = list(s)[len(s) // 2:][::-1][i]
        slf[2 * i + 1] = list(s)[:len(s) // 2][i]
    return slf
print(func(s,x))

def string_func(s,x):
    for i in range(x):
        s = func(s,x)
    return ''.join(s).strip()
    
    
def string_func(s,x):
    slf = [0]*len(s)
    for i in range(len(s) // 2):
        #print(len(s) // 2, slf)
        slf[2 * i] = list(s)[len(s) // 2:][::-1][i]
        slf[2 * i + 1] = list(s)[:len(s) // 2][i]
    x -= 1
    if x != 0: return string_func(slf,x)
    else:return ''.join(slf)
    

def string_func(s,x):
    def f(x):
        for i in range(x):
            x = func(s)
        return x
    return f

'''

