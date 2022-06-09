'''
https://www.codewars.com/kata/57e3f79c9cb119374600046b

hello "john"   => "Hello, John!"
hello "aliCE"  => "Hello, Alice!"
hello          => "Hello, World!" # name not given
hello ''       => "Hello, World!" # name is an empty String
'''


name = "aliCE"
def hello(name):

    if not name or name == '':
        return "Hello, World!"
    return f"Hello {name.lower().capitalize()}"
print(hello(name))


#1st
def hello(name=''):
    return f"Hello, {name.title() or 'World'}!"

def hello(name=""):
    return f"Hello, {name.capitalize() if name else 'World'}!"

def hello(name=None):
    if not name:
        return "Hello, World!"
    return "Hello, %s!"%(name.capitalize())