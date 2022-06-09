
# Method_1 Using %s>>
name = "Leonardo"
surname = "Da Vinci"
Occupation_1 = "Artist"
Occupation_2 = "Inventor"
Occupation_3 = "Scientist"
Occupation_4 = "Mathematician"
Occupation_5 = "Philosopher"
print ("%s %s was an %s, %s, %s, %s and %s." % (name, surname, Occupation_1, Occupation_2, Occupation_3, Occupation_4, Occupation_5))

# Method_2 Using str.format()
print (("{name} {surname} was an {Occupation_1}, {Occupation_1}, {Occupation_1}, {Occupation_1} and {Occupation_1}.").format(name = name, surname = surname, Occupation_1 = Occupation_1, Occupation_2 = Occupation_2, Occupation_3 = Occupation_3, Occupation_4 = Occupation_4, Occupation_5 = Occupation_5))

print(f'{name} {surname} was an {Occupation_1}, {Occupation_2}, {Occupation_3}, {Occupation_4} and {Occupation_5}')

print(f'{2*3}')
print(f'{name.lower()}''6')
'leonardo'


def some_function(a, b, c, d):
    print(a, b, c, d)

some_list = [1, 2, 3, 4]
some_dictionary = {'a': 1, 'b': 2, 'c': 13, 'd': 14}

def some_list_packing(*args):
    args = list(args)
    args[0] = 'I am about to'
    args[1] = 'pack lists'
    return args
#args = 'hello world'
print('some_list_packing:',some_list_packing('',''))

from collections import Counter
def some_dictionary_packing(**kwargs):
    for key in kwargs:
        print(f'{key} = {kwargs[key]}')
kword = Counter('hello world')
some_dictionary_packing()

# See how I used the f-string there?
some_dictionary_packing(a= "I", b= "am", c= "about", d= "to write..")
'''
a = I
b = am
c = about
d = to write..
'''

NewClass = type("NewClass", (object,), {"intro": "This is an awesome new class"})
n = NewClass()
print(n.intro)
"This is an awesome new class"


class NewClass(object):
    intro = "This is an awesome new class"
n = NewClass()
print(n.intro)
"This is an awesome new class"


def some_function(a, b, c, d):
    print(a, b, c, d)
    a_list = [1, 2, 3, 4]
    try:
        some_function(a_list)
    except:
        print("Put * before the input list in the function")
a, b, c, d = [1, 2, 3, 4]
some_function(a, b, c, d)