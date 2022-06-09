
def demo():
    print('This is demo function')

print(demo)        # prints <function demo at 0x11008f680>
demo()             # This is demo function

d = demo
print(d)           # prints <function demo at 0x11008f680>
d()                # This is demo functionvar = 1
print(type(d))   # <class 'int'>
print(type(d))     # <class 'function'>


def new_demo(arg):
    print(arg)  # 1
    arg()  # 2
print(new_demo(d))  # calling the function with variable

def decor(func):
    def wrapper(*args, **dkwargs):
        if dkwargs['license'] == 'userlicense':
            return func(*args, **dkwargs)
        else:
            raise ModuleNotFoundError('Module not found')
    return wrapper

@decor
def user1(*args, **dkwargs):
    print('User function called', args, dkwargs)


user1(license='userlicense')            # 1# User function called () {'license': 'userlicense'}
#user1(license='developerlicense')       # 2


myfunction = decor(user1)
myfunction(license='userlicense')# User function called () {'license': 'userlicense'}myfunction = decor(user1)
myfunction(license='developerlicense')# ModuleNotFoundError: Module not found
print(myfunction)


def outer_decor(license=None):
    def decor(func):
        def wrapper(*args, **dkwargs):
            if license == 'userlicense':
                return func(*args, **dkwargs)
            else:
                raise ModuleNotFoundError('Module not found')
        return wrapper
    return decor

@outer_decor(license='userlicense')          # 1
def user1(*args, **dkwargs):
    print('User function called', args, dkwargs)


user1()

# User function called () {}

@outer_decor(license='developerlicense')      # 2
def user2(*args, **dkwargs):
    print('User function called', args, dkwargs)

user2()

# ModuleNotFoundError: Module not found

class Decor:

    def __init__(self, license=None):
        self.license = license

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            if self.license == 'userlicense':
                return func(*args, **kwargs)
            else:
                raise ModuleNotFoundError('Module not found')
        return wrapper

@Decor(license='userlicense')
def user1(*args, **dkwargs):
    print('User function called', args, dkwargs)

@Decor(license='developerlicense')
def user2(*args, **dkwargs):
    print('User function called', args, dkwargs)


user1()
# User function called () {}

user2()

# ModuleNotFoundError: Module not found