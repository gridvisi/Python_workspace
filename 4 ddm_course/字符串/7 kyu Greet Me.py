'''
https://www.codewars.com/kata/535474308bb336c9980006f2/train/python

"riley" --> "Hello Riley!"
"JACK"  --> "Hello Jack!"
'''

name = "JACK"
name = "riley"
name.capitalize()
def greet(name):
    return "Hello " + f'{name.capitalize()}'+'!'

def greet(name):
    return f'Hello {name.title()}!'

def greet(name):
    return f"Hello {name.capitalize()}!"
print(greet(name))