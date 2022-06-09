'''
https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/
http://hangar.runway7.net/python/packing-unpacking-arguments
'''


# A Python program to demonstrate need
# of packing and unpacking

# A sample function that takes 4 arguments
# and prints them.
def fun(a, b, c, d):
    print(a, b, c, d)


# Driver Code
my_list = [1, 2, 3, 4]

# This doesn't work
fun(my_list)



#2
# A sample function that takes 4 arguments
# and prints the,
def fun(a, b, c, d):
    print(a, b, c, d)


# Driver Code
my_list = [1, 2, 3, 4]

# Unpacking list into four arguments
fun(*my_list)



#3

# Error when len(args) != no of actual arguments
# required by the funcntion

args = [0, 1, 4, 9]


def func(a, b, c):
    return a + b + c


# calling function with unpacking args
func(*args)



#4
range(3, 6)  # normal call with separate arguments
#[3, 4, 5]
args = [3, 6]
range(*args)  # call with arguments unpacked from a list
#[3, 4, 5]



#5
# A Python program to demonstrate use
# of packing

# This function uses packing to sum
# unknown number of arguments
def mySum(*args):
    return sum(args)


# Driver code
print(mySum(1, 2, 3, 4, 5))
print(mySum(10, 20))

'''
The above function mySum() does ‘packing’ to pack all the arguments 
that this method call receives into one single variable. 
Once we have this ‘packed’ variable, we can do things with it that 
we would with a normal tuple. args[0] and args[1] would give you the 
first and second argument, respectively. Since our tuples are immutable, 
you can convert the args tuple to a list so you can also modify, delete, 
and re-arrange items in i.
 

Packing and Unpacking 
Below is an example that shows both packing and unpacking. 
 
'''


# A Python program to demonstrate both packing and
# unpacking.

# A sample python function that takes three arguments
# and prints them
def fun1(a, b, c):
    print(a, b, c)


# Another sample function.
# This is an example of PACKING. All arguments passed
# to fun2 are packed into tuple *args.
def fun2(*args):
    # Convert args tuple to a list so we can modify it
    args = list(args)

    # Modifying args
    args[0] = 'Geeksforgeeks'
    args[1] = 'awesome'

    # UNPACKING args and calling fun1()
    fun1(*args)


# Driver code
fun2('Hello', 'beautiful', 'world!')

#5 is used for dictionaries

# A sample program to demonstrate unpacking of
# dictionary items using **
def fun(a, b, c):
    print(a, b, c)


# A call with unpacking of dictionary
d = {'a': 2, 'b': 4, 'c': 10}
fun(**d)


# A Python program to demonstrate packing of
# dictionary items using **
def fun(**kwargs):
    # kwargs is a dict
    print(type(kwargs))

    # Printing dictionary items
    for key in kwargs:
        print("%s = %s" % (key, kwargs[key]))


# Driver code
fun(name="geeks", ID="101", language="Python")