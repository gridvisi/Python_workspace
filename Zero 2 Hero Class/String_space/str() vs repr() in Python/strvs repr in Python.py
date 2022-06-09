#https://www.geeksforgeeks.org/str-vs-repr-in-python/
s = 'Hello, Geeks.'
print (str(s))
print (str(2.0/11.0))

s = 'Hello, Geeks.'
print (repr(s))
print (repr(2.0/11.0))

import datetime

today = datetime.datetime.now()

# Prints readable format for date-time object
print(str(today))

# prints the official format of date-time object
print(repr(today))


# Python program to demonstrate writing of __repr__ and
# __str__ for user defined classes

# A user defined class to represent Complex numbers
class Complex:

    # Constructor
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # For call to repr(). Prints object's information
    def __repr__(self):
        return 'Rational(%s, %s)' % (self.real, self.imag)

        # For call to str(). Prints readable form

    def __str__(self):
        return '%s + i%s' % (self.real, self.imag)

    # Driver program to test above


t = Complex(10, 20)

# Same as "print t"
print(str(t))
print(repr(t))