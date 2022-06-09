'''
改进的字符串格式语法（指南）
Table of Contents
“Old-school” String Formatting in Python
Option #1: %-formatting
Option #2: str.format()
f-Strings: A New and Improved Way to Format Strings in Python
Simple Syntax
Arbitrary Expressions
Multiline f-Strings
Speed
Python f-Strings: The Pesky Details
Quotation Marks
Dictionaries
Braces
Backslashes
Inline Comments
Go Forth and Format!
Further Reading
'''

name = "Eric"
age = 74
print("Hello, %s. You are %s." % (name, age))
'Hello Eric. You are 74.'

print("Hello, {}. You are {}.".format(name, age))
'Hello, Eric. You are 74.'

print("Hello, {1}. You are {0}.".format(age, name))

person = {'name': 'Eric', 'age': 74}
print("Hello, {name}. You are {age}.".format(name=person['name'], age=person['age']))

person = {'name': 'Eric', 'age': 74}
print("Hello, {name}. You are {age}.".format(**person))

first_name = "Eric"
last_name = "Idle"
age = 74
profession = "comedian"
affiliation = "Monty Python"
print(("Hello, {first_name} {last_name}. You are {age}. " +
        "You are a {profession}. You were a member of {affiliation}.") \
       .format(first_name=first_name, last_name=last_name, age=age, \
              profession=profession, affiliation=affiliation))


name = "Eric"
age = 74
print(f"Hello, {name}. You are {age}.")
'Hello, Eric. You are 74.'

#It would also be valid to use a capital letter F:

print(F"Hello, {name}. You are {age}.")
'Hello, Eric. You are 74.'

print(f"{2 * 37}")

def to_lowercase(input):
    return input.lower()

name = "Eric Idle"
print(f"{to_lowercase(name)} is funny.")
'eric idle is funny.'

#You also have the option of calling a method directly:
print(f"{name.lower()} is funny.")
'eric idle is funny.'

#You could even use objects created from classes with f-strings. Imagine you had the following class:

class Comedian:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age}."

    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.age}. Surprise!"

new_comedian = Comedian("Eric", "Idle", "74")  # __repr__ run or not depend on 74 or '74'
new_comedian = Comedian("Eric", "Idle", 74)
print(f"{new_comedian}")
'Eric Idle is 74.'

print(f"{new_comedian}")
'Eric Idle is 74.'
print(f"{new_comedian!r}")
'Eric Idle is 74. Surprise!'

name = "Eric"
profession = "comedian"
affiliation = "Monty Python"
message = (
     f"Hi {name}. "
     f"You are a {profession}. "
     f"You were in {affiliation}."
 )
print(message)

message = f"Hi {name}. " \
           f"You are a {profession}. " \
            f"You were in {affiliation}."
print(message)

message = f"""
         Hi {name}. 
        You are a {profession}. 
       You were in {affiliation}.
    """
print(message)

import timeit
timeit.timeit("""name = "Eric"
    age = 74
    '%s is %s.' % (name, age)""", number = 10000)
#0.003324444866599663

timeit.timeit("""name = "Eric"
... age = 74
... '{} is {}.'.format(name, age)""", number = 10000)
#0.004242089427570761

timeit.timeit("""name = "Eric"
... age = 74
... f'{name} is {age}.'""", number = 10000)
#0.0024820892040722242