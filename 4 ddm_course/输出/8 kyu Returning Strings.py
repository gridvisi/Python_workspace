'''
https://www.codewars.com/kata/55a70521798b14d4750000a4/train/python
'''
def greet(name):
    return "Hello, "+f"{name}"+" how are you doing today?"


def greet(name):
    return f'Hello, {name} how are you doing today?'

def greet(name):
    return "Hello, %s how are you doing today?" % name

def greet(name):
    return "Hello, {} how are you doing today?".format(name)

def greet(name):
    #Good Luck (like you need it)
    return  "Hello, {name} how are you doing today?".format(name = name)

name = 'Ryan'
print(greet(name))