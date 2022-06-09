'''
https://www.codewars.com/kata/57efab9acba9daa4d1000b30/train/python

u will be given a string(x). Clean shaved head is shown as "-" and stray hairs are shown as "/". Your task is to check the head for stray hairs and get rid of them.

You should return the original string, but with any stray hairs removed. Keep count ot them though, as there is a second element you need to return:

0 hairs --> "Clean!"
1 hair --> "Unicorn!"
2 hairs --> "Homer!"
3-5 hairs --> "Careless!"
>5 hairs --> "Hobo!"

So for this head: "------/------" you shoud return:

["-------------", "Unicorn"]
'''

def bald(s):
    dicts = {"Clean!":[0],
             "Unicorn!":[1],
             "Homer!":[2],
             "Careless!":[3,4,5],
             }
    print(s.count('/'))
    n = s.count('/')
    res = s.replace('/','-')
    #ress = [(k,v) for k,v in dicts.items()] else "Hobo!"
    ress = [k for k, v in dicts.items() if n in v]
    return [res,ress[0] if ress else "Hobo!"]
    #[i for i in s if i == '/']

s = "------/------"
s = "--/-/-/---/-/--/-"
s = "/-----/-"
print(bald(s))

#1st
def bald(s):
    hair_names = {
        0: "Clean!",
        1: "Unicorn!",
        2: "Homer!",
        3: "Careless!",
        4: "Careless!",
        5: "Careless!",
    }
    return [s.replace("/","-"),"Hobo!"] if s.count("/") > 5 else [s.replace("/","-"), hair_names[s.count("/")]]


#2nd
CONFIG = {0: "Clean!", 1: "Unicorn!", 2: "Homer!", 3: "Careless!", 4: "Careless!", 5: "Careless!"}

def bald(s):
    return ['-'*len(s), CONFIG.get(s.count("/"), "Hobo!")]