'''
https://www.codewars.com/kata/57eae20f5500ad98e50002c5/solutions/python


'''

def no_space(x):
    return ''.join([i for i in x if i != ' '])

def no_space(x):
    return x.replace(' ' ,'')

def no_space(x):
    return "".join(x.split())

def no_space(x):
    str_char = ''
    for i in range(len(x)):
        if x[i] == ' ':
            continue
        else:
            str_char = str_char + x[i]
    return str_char