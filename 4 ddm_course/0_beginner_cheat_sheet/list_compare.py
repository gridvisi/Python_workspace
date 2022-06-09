
#What is the output of the code snippet below?
my_list = "7 77 55 2345"
my_second_list = my_list.split()
print(my_second_list)
print(max(my_second_list))
#Wrong!👎

#The split() methods returns a string. Hence the right answer is 77 .

'''
https://www.tutorialspoint.com/python/python_lists.htm
1、How many Python keywords are not lowercase?

5
3
1
2
4

Only three Python keywords are not lowercase: None , True and False .
https://www.programiz.com/python-programming/keyword-list

2、What is the output of the code snippet below?
a = True
print(('A', 'B')[a == False])

B

3、What is the output of the code snippet below?
print((True==False==True)==False)
Correct!👍

First, True==False==True evaluates as False . Then False==False evaluates as True .

4、What is the output of the code snippet below?
*a, b, c = range(5)
print(*a)

0 1 2
1 2 3 4 5
2 3 4
It will throw a ValueError error

5、Which function only accepts integers as arguments?

min()
any()
ord()
chr()
None of the above

6、Python has built-in support for arrays.

False
True


7、Which syntax below won't work to add a new item to the dictionary my_dict? (Python 3.5+)

my_dict.add('new_key','new_value')
my_dict.update({'new_key':'new_value'})
{**my_dict, 'new_key': new_val}
my_dict['new_key'] = 'new_val'​

8、What is the output of the code snippet below?
oct(7)
oct("7")

07
0o7

Syntax Error
07

0o7
SyntaxError

None of the above


9、Considering the code snippet below, which function call is not allowed? (3.8+)
def f(a=2, /):
pass

f(1)
f()
f(a=1)

10、What is the output of the code snippet below?
my_list = []
print(bool(my_list))

True

11、What is the correct command to shuffle the list below?
fruit=['apple', 'banana', 'papaya', 'cherry']

random.shuffle(fruit)
fruit.shuffle()
random.shuffleList(fruit)
shuffle(fruit)


13、What is the output of the code snippet below?
class Test1 (object):
pass
class Test2 (Test1):
pass
a = Test1()
b = Test2()
print(type(b) is Test1)

False

14、What is the output of the code snippet below?
k=lambda x,y : x%y
print(k(36,32)+ k(15,10))

2
9
8
5
None of the above

15、Which statement is correct?

A class is an instance of a metaclass.
A metaclass is an instance of a class
就像一个 "普通 "的类定义了该类实例的行为，一个元类定义了类和它们的实例的行为。
https://python-course.eu/oop/metaclasses.php


16、A function can access a variable defined out of the function even if is not set as global.

False
True


17、Which data structure stores items in a Last-In/First-Out manner?
Correct!👍

The stack stores items in a Last-In/First-Out manner


18、What is the output of the code snippet below?
def foo(**kwargs):
     return kwargs

foo(1)
1
It will throw a TypeError.
(1)
{1}

19、Which one is not a type of inheritance?

Multiple inheritance
Indirect inheritance
Multilevel inheritance

20、Which operator function corresponds to the syntax below?
del obj[k]

del(obj, k)
suppr(obj, k)
delete(obj, k)
delitem(obj, k)

21、What is the output of the code snippet below?
print([5, 1] > [4, 2, 4, 5])
Wrong!👎

When used against lists, comparison operators compare the first element of each list. Here, as 5 is greater than 4 , True will be printed.

22、What is the output of the code snippet below?
my_list = "7 77 55 2345"
my_second_list = my_list.split()

print(max(my_second_list))
Wrong!👎

The split() methods returns a string. Hence the right answer is 77 . 

23All iterables store all elements in memory.
Not all iterables store all element in memory. For instance, whilst lists and strings store all elements in memories, Python 3's range() generate them on the fly as needed. 

https://stackoverflow.com/questions/36619152/do-pythons-iterables-really-store-all-values-in-memory






All iterables store all elements in memory.
Correct!👍

Not all iterables store all element in memory. 
For instance, whilst lists and strings store all elements in memories, 
Python 3's range() generate them on the fly as needed. (
stackoverflow.com/questions/36619152/do-pythons-iterables...)

https://stackoverflow.com/questions/36619152/do-pythons-iterables-really-store-all-values-in-memory
'''

#3 What is the output of the code snippet below?
*a, b, c = range(5)
print(*a)

#0 1 2
#1 2 3 4 5
#2 3 4
#It will throw a ValueError error