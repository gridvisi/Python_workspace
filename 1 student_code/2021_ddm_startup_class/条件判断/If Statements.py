
'''
If Statements
If statements are at the heart of almost all decision-making in programming.
If statements allow you to treat some data differently than the rest of your data.

In [1]:

'''

# Example.
names = ['devin', 'killian', 'eric', 'matt', 'psalm', 'roger']

for name in names:
    print(f"Hello, {name}.")
    if name == 'matt':
        print("  Please, no puns today!")

'''
Hello, devin.
Hello, killian.
Hello, eric.
Hello, matt.
  Please, no puns today!
Hello, psalm.
Hello, roger.
Conditional Statements
Conditional statements evaluate to True or False.

In [1]:
True
Out[1]:
True
In [3]:
False
Out[3]:
False
In [4]:
5 == 5
Out[4]:
True
In [6]:
3 == 5
Out[6]:
False
In [12]:
age = 17

age == 18
age > 18
age < 18
age >= 18
age <= 18
age != 18 # age is not equal to 18?


'''
artists = ['prince', 'frieda kahlo', 'stan lee', 'isaac asimov']

#'stan lee' in artists

all_students = [...]

eligible_voters = []

for student in all_students:
    if student.age >= 18:
        eligible_voters.append(student)

#Simple if statements
#You're only interested in one condition.

#In [17]:
ages = [16, 18, 11, 17, 16, 17, 19, 18, 21, 45, 89, 1, 7]

for age in ages:
    if age >= 18:
        print("Hey, did you know you can vote?!")

'''
Hey, did you know you can vote?!
Hey, did you know you can vote?!
Hey, did you know you can vote?!
Hey, did you know you can vote?!
Hey, did you know you can vote?!
Hey, did you know you can vote?!
If-else statements
You're interested in one condition, but you also want to do something else 
with everyone who doesn't meet that condition.

In [18]:

'''
ages = [16, 18, 11, 17, 16, 17, 19, 18, 21, 45, 89, 1, 7]

for age in ages:
    if age >= 18:
        print("Hey, did you know you can vote?!")
    else:
        print("Grow up! And some day you'll be able to vote.")
'''
Grow up! And some day you'll be able to vote.
Hey, did you know you can vote?!
Grow up! And some day you'll be able to vote.
Grow up! And some day you'll be able to vote.
Grow up! And some day you'll be able to vote.
Grow up! And some day you'll be able to vote.
Hey, did you know you can vote?!
Hey, did you know you can vote?!
Hey, did you know you can vote?!
Hey, did you know you can vote?!
Hey, did you know you can vote?!
Grow up! And some day you'll be able to vote.
Grow up! And some day you'll be able to vote.
If-elif-else statements
You're interested in several specific conditions.

In [22]:
'''
ages = [16, 18, 11, 17, 16, 17, 19, 18, 21, 45, 89, 1, 7]

for age in ages:
    if age >= 18:
        print("Hey, did you know you can vote?!")
    elif age <= 16:
        print("Grow up! And some day you'll be able to vote.")
    else:
        print("Please get ready to register to vote as soon as you turn 18!")
'''
Grow up! And some day you'll be able to vote.
Hey, did you know you can vote?!
Grow up! And some day you'll be able to vote.
Please get ready to register to vote as soon as you turn 18!
Grow up! And some day you'll be able to vote.
Please get ready to register to vote as soon as you turn 18!
Hey, did you know you can vote?!
Hey, did you know you can vote?!
Hey, did you know you can vote?!
Hey, did you know you can vote?!
Hey, did you know you can vote?!
Grow up! And some day you'll be able to vote.
Grow up! And some day you'll be able to vote.
If-if-if statements
You want to test a bunch of situations, and any or all conditions can be met.

In [21]:
'''
philip_pizza = ['sardines', 'onions']

# Pizza making code.
if 'pepperoni' in philip_pizza:
    print("Adding pepperoni.")
if 'sardines' in philip_pizza:
    print("Adding sardines.")
if 'mushrooms' in philip_pizza:
    print("Adding mushrooms.")
if 'onions' in philip_pizza:
    print("Adding onions.")
