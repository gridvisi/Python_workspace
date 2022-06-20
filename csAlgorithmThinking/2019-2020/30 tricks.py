'''
30 Simple Tricks to Level Up Your Python Coding
Better Python  Yong Cui, Ph.D.
Mar 20 · 13 min read

Photo by Lindsay Henwood on Unsplash
As a general-purpose programming language, Python has penetrated to almost all industrial and academic fields. Based on my observation of Python programming in the areas of biomedical sciences, I realize that a considerable number of Python programmers, myself included, come from various programming backgrounds, such as Matlab, C, C++, Java, JavaScript, and Swift, not to mention some having no prior coding experience.
With Python being their “foreign” language, they may not have a systematic training on Python coding, and might not know the idiomatic way for their Python development.
But don’t get me wrong — they can still write excellent code by implementing the same functionalities in different ways, as long as the code can satisfy the intended purposes. Thus, to me, it’s acceptable to write non-idiomatic Python programs.
However, just like I’m always working to improve my English accent as a foreigner in the United States, I want my Python code to be idiomatic as little as possible. In this article, I’m sharing some idiomatic usages that I have accumulated over the last several years, which I hope will help level up your Python coding.
1. Slice a Sequence
Some common sequence types are lists, tuples, and strings. We can create a sequence by slicing another sequence. The following functionalities use a list as an example, but they can also apply to tuples, strings, and other sequence types (e.g., bytes).
'''

a = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# Using a range, [start, end)
a[1:3]  #[2, 4]

# Using a range with a step
a[1:9:2]  #[2, 6, 10, 14]

# Leave out the start = an implicit start of 0
a[:5]  #[0, 2, 4, 6, 8]

# Leave out the stop = an implict end to the very last item
a[9:] #[18, 20]

# Entire list
a[:]  #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

#2. Reverse a Sequence:Sometimes, we want to reverse a sequence. Although we can use
# a for-loop to achieve it, there is a straightforward way. Similarly, as above, when
# a functionality is available to a sequence, it usually means that strings, tuples,
# and lists all support this functionality.

a = (1, 2, 3, 4, 5)
a[::-1] #(5, 4, 3, 2, 1)
b = 'start'
b[::-1] #'trats'

#3. Access an Element in a Sequence Using the Reverse Index
#If we want to access some elements towards the end of a sequence,
# it’s easier to count backward. In a Python sequence, the last element has
# an index of -1, the one before it has an index of -2, and so on.
a = 'Hello World!'
# instead of using a[len(a)-1]
a[-1] #'!'

# in combination with slicing
a[-5:-1] #'orld'

#4. Multiple Assignments
#When we want to assign certain values to several variables, we can do multiple
# assignments. We can apply the same idiom to swap two variables or two elements
# in a list. Behind the scenes, this feature is closely related to the tuple unpacking that is introduced later in this article.
# instead of doing a = 8; b = 5
a, b = 8, 5
print(f'a is {a}; b is {b}')
print(a is 8, b is 5)

# Swap two variables
a, b = b, a
print(f'a is {a}; b is {b}')
print(a is 5, b is 8)

# Swap the first and last elements in a list
numbers = [1, 2, 3, 4, 5]
numbers[0], numbers[-1] = numbers[-1], numbers[0]
numbers
#[5, 2, 3, 4, 1]


#5. Check if a Sequence Is Empty
#Some operations only make sense when the sequence (e.g., list, tuple)
# isn’t empty, and thus we need to check that before applying the proper operations.
# To do that, we can just use the not keyword to negate the sequence (e.g., not []),
# which will evaluate as True if the sequence is not empty. Besides,
# we can do the same thing with the other two common data types: dict and set.
empty_list = [(), '', [], {}, set()]
for item in empty_list:
  if not item:
    print(f'Do something with the {type(item)}')
'''
Do something with the <class 'tuple'>
Do something with the <class 'str'>
Do something with the <class 'list'>
Do something with the <class 'dict'>
Do something with the <class 'set'>
'''


#6. List Comprehensions
#A handy feature in Python is the list comprehension, which we can construct
# a list very conveniently with. The list comprehension has a general format of
# [some_expression for element in iterable if some_condition].
a = [1, 2, 3, 4, 5]
print([x*2 for x in a])  #[2, 4, 6, 8, 10]

print([x*3 for x in a if x%2 == 1])
#[3, 9, 15]

#7. Set Comprehensions
#The usage of the set comprehension is similar to the list comprehension,
# as above. The difference is that we’ll use the curly brackets instead of
# square brackets. Also, the duplicate elements will get removed by the definition
# of the set data type.

a = [1, -2, 2, -3, 3, 4, 4, 5, 5, 5]
print({x*x for x in a})
#{1, 4, 9, 16, 25}

#8. Dict Comprehensions
#Besides the list and set comprehensions, the comprehension feature is also
# available to the creation of the dictionary data type. A dict consists of
# key-value pairs, so the dict comprehension involves the specification of keys and values,
# which are separated by a colon.
a = [1, 2, 3, 4, 5]
print({x: x*x for x in a})
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#9. Generator Expression
#Generators in Python are a convenient way to create iterators. As generators are “lazy” (i.e., yield the needed item when requested), they’re very memory-efficient. One particular way to create generators is called generator expression, which is syntactically similar to the list comprehension, except for using parentheses instead of square brackets.
#In the below examples, the parentheses are optional when generators are directly used in functions that can take iterables.
sum(x**2 for x in range(100))
#328350
max((x*x for x in range(100)))
#9801

#10. Unpack a Tuple
#Tuples are a very common data structure in Python. They’re just groups of related values, and common usage of tuples involves accessing their elements. We can access these elements using indices, but unpacking is a more convenient way. Related to its usage, we can use an underscore to indicate the elements that we don’t need and use an asterisk to assign the remaining elements other than the named ones.
items = (0, 'b', 'one', 10, 11, 'zero')
a, b, c, d, e, f = items
print(f)
#zero
a, *b, c = items
print(b)
#['b', 'one', 10, 11]

*_, a, b = items
print(a)

#11. Use Enumerate() In for Loops
#The enumerate() function takes in an iterable to create an iterator. Besides, it can track the number of iterations. We can optionally set the start of the counting. The default counting starts at 0.
students = ('John', 'Mary', 'Mike')
for i, student in enumerate(students):
  print(f'Iteration: {i}, Student: {student}')
'''
Iteration: 0, Student: John
Iteration: 1, Student: Mary
Iteration: 2, Student: Mike
'''
for i, student in enumerate(students, 35001):
  print(f'Student Name: {student}, Student ID #: {i}')
'''
Student Name: John, Student ID #: 35001
Student Name: Mary, Student ID #: 35002
Student Name: Mike, Student ID #: 35003
'''

#12. Use Reversed() In for Loops
#The reversed() function is often used in the for loops as a way to create an iterator in the reversed order of the original iterable.
tasks = ['laundry', 'picking up kids', 'gardening', 'cooking']
for task in reversed(tasks):
  print(task)
'''
cooking
gardening
picking up kids
laundry
'''

#13. The Zip() Function
#The zip() function is useful to join multiple iterators on a one-to-one match basis. If certain iterators exceed the shortest one, they get truncated. This function returns an iterator, and thus it is frequently used in an iteration. We can also use the zip() function to unzip an iterator using the asterisk sign and assign the unzipped items to variables.
students = ('John', 'Mary', 'Mike')
ages = (15, 17, 16)
scores = (90, 88, 82, 17, 14)
for student, age, score in zip(students, ages, scores):
  print(f'{student}, age: {age}, score: {score}')
'''
John, age: 15, score: 90
Mary, age: 17, score: 88
Mike, age: 16, score: 82
'''
zipped = zip(students, ages, scores)
a, b, c = zip(*zipped)
print(b)
#(15, 17, 16)

#14. Lambdas for Sorting
#Lambdas are anonymous functions that can take multiple arguments with a single-line expression. One of its common usages is to set as the key argument in the sorted() function. Besides this, lambdas are often used in some functions (e.g., max(), map()) where a one-line expression is applicable to replace a regular function using the def keyword.
students = [{'name': 'John', 'score': 98}, {'name': 'Mike', 'score': 94}, {'name': 'Jennifer', 'score': 99}]
sorted(students, key=lambda x: x['score'])
#[{'name': 'Mike', 'score': 94}, {'name': 'John', 'score': 98}, {'name': 'Jennifer', 'score': 99}]

#15. Shorthand Conditional Assignment
#This feature is mostly a syntax sugar. When you need to assign a value to a variable based on a certain condition, we can use a shorthand assignment using this general form: y = x if condition_met else another_x.
some_condition = True
# the expanded format
if some_condition:
    x = 5
else:
    x = 3
print(f'x is {x}')
#x is 5
# the shorthand way
x = 5 if some_condition else 3
print(f'x is {x}')
#x is 5

#16. Membership Testing in a Collection
#Sometimes, we need to test if a certain element exists in a collection before we want to apply the operations to the collection or the matched item. The idiomatic way is to use the in keyword.
a = ('one', 'two', 'three', 'four', 'five')
if 'one' in a:
    print('The tuple contains one.')

#The tuple contains one.
b = {0: 'zero', 1: 'one', 2: 'two', 3: 'three'}
if 2 in b.keys():
  print('The dict has the key of 2.')
#The dict has the key of 2.

#17. Use Get() to Retrieve a Value in a Dictionary
#We normally can specify the key in square brackets to retrieve the value for the key. However, it will raise an error when the key doesn’t exist in the dictionary. Certainly, we can use try/except to solve this issue. Instead, we can use the get() method that allows us to use a default value when the key isn’t in the dictionary.
number_dict = {0: 'zero', 1: 'one', 2: 'two', 3: 'three'}
number_dict[5]
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 5
'''
number_dict.get(5, 'five')
#'five'

#18. Get the Key Whose Value Is Maximal in a Dictionary
#For a dictionary, we sometimes need to find out the key whose value is maximal. We can first find out the maximal value’s index in a list of all the values, and then find the corresponding key from another list that stores all the keys. Alternatively, an easier way is to specify the key argument in the max() function.
#For simplicity, we don’t consider scenarios where the maximal values may have duplicates. Besides, the same approach can be applied to finding the key with minimal value using the min() function.
model_scores = {'model_a': 100, 'model_z': 198, 'model_t': 150}
# workaround
keys, values = list(model_scores.keys()), list(model_scores.values())
keys[values.index(max(values))]
#'model_z'

# one-line
max(model_scores, key=model_scores.get)
'model_z'

#19. Debug With the Print() Function
#For smaller projects, we can always use the print() function to help us debug. We also use this function a lot for teaching purposes. There are a couple of tricks that we use frequently with the print() function. The first is to end the string other than the default newline, and the second is to use an f-string, which allows us to create a string containing some expressions.
for i in range(5):
    print(i, end=', ' if i < 4 else '\n')

#0, 1, 2, 3, 4

for i in range(5):
    print(f'{i} & {i*i}', end=', ' if i < 4 else '\n')

#0 & 0, 1 & 1, 2 & 4, 3 & 9, 4 & 16

#20. Walrus Operator
#The walrus operator (:=) is a new feature available in Python 3.8+. It’s just another name for assignment expression — assignment to a variable within an expression. Usually, when an expression uses a variable, the variable has to be declared earlier. With the walrus operator, the variable assignment can be included in the expression, and the variable is available to use right away.
a = ['j', 'a', 'k', 'd', 'c']
if (n := len(a))%2 == 1:
    print(f'The number of letters is {n}, which is odd.')
#The number of letters is 5, which is odd.

#21. Split a String
#When we work with strings, it’s a common task to separate the strings into a list of words. In this case, we can use the split() function, which takes a separator and optionally the maximal splits. A related function is the rsplit() function, which has a similar functionality except that it starts the splitting from the right to satisfy the maximal splits requirement when set.
sentence = 'this is, a python, tutorial, about, idioms.'
sentence.split(', ')
#['this is', 'a python', 'tutorial', 'about', 'idioms.']
sentence.split(', ', 2)
#['this is', 'a python', 'tutorial, about, idioms.']

sentence.rsplit(', ')
#['this is', 'a python', 'tutorial', 'about', 'idioms.']
sentence.rsplit(', ', 2)
#['this is, a python, tutorial', 'about', 'idioms.']

#22. Join Strings in an Iterable
#When working with strings, we sometimes need to create a single string by joining a series of strings contained in an iterable (e.g., list, tuple). In this case, we can use the join() function that is called by the desired separator.
words = ('Hello', 'Python', 'Programmers')
'!'.join(words)
'Hello!Python!Programmers'

words_dict = {0: 'zero', 1: 'one', 2: 'two', 3: 'three'}
'&'.join(words_dict.values())
'zero&one&two&three'

#23. The Map() Function
#The map() function is a high-order function (i.e., a function that uses a function as an argument or returns a value as its output). It has a general format of map(function, iterables), which will apply the function to the iterable(s) and return a map object, which is an iterator. The number of iterables should match the number of needed arguments for the function.
#In the example below, the built-in pow() function expects two arguments. Certainly, a custom function can be used as well. As a side note, when we use the map() function to create a list, we can probably use the list comprehensions to achieve the same effect.
numbers = (1, 2, 4, 6)
indices = (2, 1, 0.5, 2)
# use map()
list(map(pow, numbers, indices))
#[1, 2, 2.0, 36]

# list comprehensions
[pow(x, y) for x, y in zip(numbers, indices)]
#[1, 2, 2.0, 36]

#24. The Filter() Function
#The filter() function is to filter a sequence using the specified function or lambda function. This function returns a filter object, which is an iterator. Overall, its usage is very similar to the map() function.
def good_word(x: str):
    has_vowels = not set('aeiou').isdisjoint(x.lower())
    long_enough = len(x) > 7
    good_start = x.lower().startswith('pre')
    return has_vowels & long_enough & good_start
words = ['Good', 'Presentation', 'preschool', 'prefix']
list(filter(good_word, words))
#['Presentation', 'preschool']

#25. Find Out the Most Frequent Element in a List
#When we use a list to record something that can have duplicate elements,
#say tracking the winners of a series of games, it’s a relevant task to find out
# who has won for the most times. It can be done by using the max() function by
# specifying the key argument, which will find out the maximal value by the count
# of the element in the set.
winnings = ['John', 'Billy', 'Billy', 'Sam', 'Billy', 'John']
max(set(winnings), key = winnings.count)
'Billy'

#26. Track the Frequencies of the Elements in a List
#Following up on the above example, we also want to know how non-champion players are doing
# for the contest such so we can find out the second and third places. To do that,
# we need to find out how many winnings each player has. We can use dictionary comprehension
# and the sorted() function with a lambda function.
winnings = ['John', 'Billy', 'Billy', 'Sam', 'Billy', 'John']
tracked = {item: winnings.count(item) for item in set(winnings)}
sorted(tracked.items(), key=lambda x: x[1], reverse=True)
#[('Billy', 3), ('John', 2), ('Sam', 1)]

#27. Check the Type of an Object
#Checking an object’s type is part of the introspection topic in Python. Sometimes, we need to know if an object is of a certain type before we apply the corresponding function. To do that, we can use the type() or isinstance() function, with the latter being a more flexible method that allows one-to-many checking.
def check_type(number):
  if type(number) == int:
      print('do something with an int')
  if isinstance(number, (int, float)):
      print('do something with an int or float')
'''
check_type(5)
do something with an int
do something with an int or float

check_type(4.2)
do something with an int or float
'''
#The Any() Function
#Suppose we have a list of records tracking John’s arrival time to the work. One use case is that we want to know if he has any late arrival this week, in which case, the any() function is very handy. This function returns True if any of the elements in a boolean list is True.
arrival_hours = {'Mon': 8.5, 'Tue': 8.75, 'Wed': 9, 'Thu': 8.5, 'Fri': 8.5}
arrival_checks = [x>8.75 for x in arrival_hours.values()]
any(arrival_checks)
#True

#29. The All() Function
#Following up on the same example above, we also want to know if he arrived at the work always before 9:30 for the whole week. To test if it’s the case, we can use the all() function, which returns True only if all of the elements in a boolean list are True.
arrival_checks_all = [x<9.5 for x in arrival_hours.values()]
all(arrival_checks)
#True

#30. Use the With Keyword on a File
#When we are dealing with a file, we need to open it, process the content, and then close it. If you don’t close the file after the use, the file may not be available for some time. The with keyword is very useful in this case. As shown below, the file will be automatically closed after the use.
with open('a_file.txt') as file:
    pass

file.closed
#True

'''
Closing Thoughts
This article isn’t intended to provide an exhaustive list of the idiomatic usages in Python programming. Instead, it’s trying to show you some common idioms, most of which we can apply to our everyday Python coding.
I must have missed some idioms in Python coding in this article. Therefore, you’re very welcome to leave your responses if you think of anything handy to share with other Python programmers.
Programming
Software Engineering
Python
Artificial Intelligence
Machine Learning
322 claps
'''
