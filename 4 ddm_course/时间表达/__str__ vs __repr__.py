
'''
https://switowski.com/blog/str-vs-repr
Every now and then, when I go back to writing Python code after a break, a question comes to mind:
What message should I put into the __str__ and the __repr__ functions?
When you search for the difference between them, you will find out that __str__ should be human readable and __repr__ should be unambiguous (as explained in this StackOverflow question). It’s a great, detailed answer. But for some reason, it never really stuck with me. I’m not the smartest developer and sometimes to remember something, I need a very simple example. What I actually found helpful was written straight in the documentation of the repr() function:
For many types, this function makes an attempt to return a string that would yield an object with the same value when passed to eval()
An excellent example of what it means, is the datetime module:
'''

import datetime
now = datetime.datetime.now()
str(now)
'2019-01-21 19:26:40.820153'
repr(now)
'datetime.datetime(2019, 1, 21, 19, 26, 40, 820153)'

timestamp = datetime.datetime(2019, 1, 21, 19, 26, 40, 820153)
print(now == timestamp)
#True
# But!
print(id(now) == id(timestamp))
#False

#So how can you use it in your own classes? For instance, if you are writing a class Car that
# has the attributes color and brand and is initialized in the following way:

class Car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color

    def year_produce(self,year):
        self.year = year

red_volvo = Car(brand='volvo', color='red')
print('car:',red_volvo.brand,red_volvo.color)
#red_volvo = Car(brand='volvo', color='red',year = '2020')
red_volvo.year_produce('2020')
print(red_volvo.year)

#then this is what the __repr__ function for the car should return:

print(repr(red_volvo))
"Car(brand='volvo', color='red')"

#It’s not always possible to write the __repr__ function that can recreate a given object,
# but simply keeping in mind those examples with datetime and Car has helped me to remember the
# difference between the __repr__ and __str__.
#I found out about this trick in “Python Tricks” book, by Dan Bader. If you haven’t heard of it,
# it’s a great source of intermediate-level pieces of knowledge about Python.
# I’m in no way associated with Dan, but his book was one of the most enjoyable
# Python technical reads I’ve had in a long time.

class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []  # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

'''
d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks
['roll over']
e.tricks
['play dead']

'''
class C:
 @classmethod
 def f(cls):
    pass
 @classmethod
 @property
 def age(cls):
    print("haha")
if __name__ == "__main__":
 c=C()
 c.age
 print("over")