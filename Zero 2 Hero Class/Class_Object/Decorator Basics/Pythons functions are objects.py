# https://stackoverflow.com/questions/739654/how-to-make-function-decorators-and-chain-them-together/1594484#1594484

from functools import wraps

def makebold(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return "<b>" + fn(*args, **kwargs) + "</b>"
    return wrapper

def makeitalic(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return "<i>" + fn(*args, **kwargs) + "</i>"
    return wrapper

@makebold
@makeitalic
def hello():
    return "hello world"

@makebold
@makeitalic
def log(s):
    return s

print (hello())        # returns "<b><i>hello world</i></b>"
print (hello.__name__ )# with functools.wraps() this returns "hello"
print (log('hello'))   # returns "<b><i>hello</i></b>"


def shout(word="yes"):
    return word.capitalize()+"!"

print(shout())
# outputs : 'Yes!'

# As an object, you can assign the function to a variable like any other object
scream = shout

# Notice we don't use parentheses: we are not calling the function,
# we are putting the function "shout" into the variable "scream".
# It means you can then call "shout" from "scream":

print(scream())
# outputs : 'Yes!'

# More than that, it means you can remove the old name 'shout',
# and the function will still be accessible from 'scream'

del shout
try:
    print(shout())
except NameError as e:
    print(e)
    #outputs: "name 'shout' is not defined"

print(scream())
# outputs: 'Yes!'


def talk():

    # You can define a function on the fly in "talk" ...
    def whisper(word="yes"):
        return word.lower()+"..."

    # ... and use it right away!
    print(whisper())

    # You call "talk", that defines "whisper" EVERY TIME you call it, then
    # "whisper" is called in "talk".
    talk()
    # outputs:
    # "yes..."

# But "whisper" DOES NOT EXIST outside "talk":

    try:
        print(whisper())
    except NameError as e:
        print(e)
    #outputs : "name 'whisper' is not defined"*
    #Python's functions are objects



# A decorator is a function that expects ANOTHER function as parameter
def my_shiny_new_decorator(a_function_to_decorate):

    # Inside, the decorator defines a function on the fly: the wrapper.
    # This function is going to be wrapped around the original function
    # so it can execute code before and after it.
    def the_wrapper_around_the_original_function():

        # Put here the code you want to be executed BEFORE the original function is called
        print("Before the function runs")

        # Call the function here (using parentheses)
        a_function_to_decorate()

        # Put here the code you want to be executed AFTER the original function is called
        print("After the function runs")

    # At this point, "a_function_to_decorate" HAS NEVER BEEN EXECUTED.
    # We return the wrapper function we have just created.
    # The wrapper contains the function and the code to execute before and after. It’s ready to use!
    return the_wrapper_around_the_original_function

# Now imagine you create a function you don't want to ever touch again.
def a_stand_alone_function():
    print("I am a stand alone function, don't you dare modify me")

a_stand_alone_function()
#outputs: I am a stand alone function, don't you dare modify me

# Well, you can decorate it to extend its behavior.
# Just pass it to the decorator, it will wrap it dynamically in
# any code you want and return you a new function ready to be used:

a_stand_alone_function_decorated = my_shiny_new_decorator(a_stand_alone_function)
a_stand_alone_function_decorated()
#outputs:
#Before the function runs
#I am a stand alone function, don't you dare modify me
#After the function runs
@my_shiny_new_decorator
def another_stand_alone_function():
    print("Leave me alone")

another_stand_alone_function()
#outputs:
#Before the function runs
#Leave me alone
#After the function runs


# It’s not black magic, you just have to let the wrapper
# pass the argument:

def a_decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(arg1, arg2):
        print("I got args! Look: {0}, {1}".format(arg1, arg2))
        function_to_decorate(arg1, arg2)

    return a_wrapper_accepting_arguments


# Since when you are calling the function returned by the decorator, you are
# calling the wrapper, passing arguments to the wrapper will let it pass them to
# the decorated function

@a_decorator_passing_arguments
def print_full_name(first_name, last_name):
    print("My name is {0} {1}".format(first_name, last_name))


'''
Taking decorators to the next level
Passing arguments to the decorated function
'''
print_full_name("Peter", "Venkman")
# outputs:
# I got args! Look: Peter Venkman
# My name is Peter Venkman


'''
Decorating methods
One nifty thing about Python is that methods and functions 
are really the same. The only difference is that methods expect that 
their first argument is a reference to the current object (self).

That means you can build a decorator for methods the same way! 
Just remember to take self into consideration:
'''


def method_friendly_decorator(method_to_decorate):
    def wrapper(self, lie):
        lie = lie - 3  # very friendly, decrease age even more :-)
        return method_to_decorate(self, lie)

    return wrapper


class Lucy(object):

    def __init__(self):
        self.age = 32

    @method_friendly_decorator
    def sayYourAge(self, lie):
        print("I am {0}, what did you think?".format(self.age + lie))

l = Lucy()
l.sayYourAge(-3)
# outputs: I am 26, what did you think?


def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    # The wrapper accepts any arguments
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print("Do I have args?:")
        print(args)
        print(kwargs)
        # Then you unpack the arguments, here *args, **kwargs
        # If you are not familiar with unpacking, check:
        # http://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/
        function_to_decorate(*args, **kwargs)

    return a_wrapper_accepting_arbitrary_arguments


@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("Python is cool, no argument here.")


function_with_no_argument()


# outputs
# Do I have args?:
# ()
# {}
# Python is cool, no argument here.

@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print(a, b, c)


function_with_arguments(1, 2, 3)


# outputs
# Do I have args?:
# (1, 2, 3)
# {}
# 1 2 3

@a_decorator_passing_arbitrary_arguments
def function_with_named_arguments(a, b, c, platypus="Why not ?"):
    print("Do {0}, {1} and {2} like platypus? {3}".format(a, b, c, platypus))


function_with_named_arguments("Bill", "Linus", "Steve", platypus="Indeed!")


# outputs
# Do I have args ? :
# ('Bill', 'Linus', 'Steve')
# {'platypus': 'Indeed!'}
# Do Bill, Linus and Steve like platypus? Indeed!

class Mary(object):

    def __init__(self):
        self.age = 31

    @a_decorator_passing_arbitrary_arguments
    def sayYourAge(self, lie=-3):  # You can now add a default value
        print("I am {0}, what did you think?".format(self.age + lie))


m = Mary()
m.sayYourAge()
# outputs
# Do I have args?:
# (<__main__.Mary object at 0xb7d303ac>,)
# {}
# I am 28, what did you think?