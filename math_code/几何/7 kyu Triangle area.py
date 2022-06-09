# https://www.codewars.com/kata/59bd84b8a0640e7c49002398/train/python


def t_area(t_str):
    return (len(t_str.split('\n')[-2])//2)**2 / 2

t_str = '\n.\n. .\n. . .\n'
print(t_area(t_str))

def t_area(t):
    return t.count(' ') - (t.count('\n') - 2) / 2

def t_area(t_str):
    return t_str.strip().count('\n')**2 / 2

def t_area(t_str):
    count = 0
    for i in t_str:
        if i == '\n':
            count += 1
    length = count -2
    breath = count - 2
    Area = (length * breath) / 2
    return Area