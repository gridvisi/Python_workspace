'''
https://www.codewars.com/kata/577bd026df78c19bca0002c0/train/python

S is misinterpreted as 5
O is misinterpreted as 0
I is misinterpreted as 1
'''

def correct(s):
    repl = {"5": "S", "0": "O", "1": "I"}

    return [s.replace(k,v) for k,v in repl.items()]



def correct(s):
    repl = {"5": "S", "0": "O", "1": "I"}
    for c in s:
        if c in repl.keys():
            print(c,repl[c])
            s.replace(c, repl[c])
    return s
s = "L0ND0N"
print(s.replace('0','O'))

print(correct(s))

def correct(s):
    repl = {"5":"S", "0":"O","1":"I"}
    return ''.join([repl[i] if i in repl.keys() else i for i in s])