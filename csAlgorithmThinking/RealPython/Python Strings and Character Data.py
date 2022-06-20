# https://realpython.com/python-strings/#built-in-string-methods
# https://realpython.com/quizzes/python-strings/viewer/

# https://realpython.com/quizzes/
'''
s = 'foo'
t = 'bar'
print('barf' in 2 * (s + t))
What is the output of the print() function call?


False


True

Correct

The + operator concatenates strings and the * operator creates multiple copies. The result of 2 * (s + t) is 'foobarfoobar', which does contain the string 'barf'.

Review: String Operators

'''

#2
'''
What is the result of this statement?

print(ord('foo'))

102 111 111


102


324


It raises an exception

Correct

The ord() function returns the integer value for a given character. But you can only specify a single character (a string of length 1):

>>> print(ord('f'))
102

>>> print(ord('foo'))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: ord() expected a character, but string of length 3 found
Review: Built-in String Functions
'''

#3
'''
What is the slice expression that gives every third character of string s, starting with the last character and proceeding backward to the first?

s[::-1]
Incorrect
Expected output 'zwtqnkheb852' for input string 
'0123456789abcdefghijklmnopqrstuvwxyz'

This is what we expected to see:
s[::-3]

The third index in the slice expression is -3, which indicates every third character stepping backward.

The first and second indices should be -1 (the last character) and 0 (the first character). Either of these can be allowed to default.

Any of these expressions will produce the correct answer:

s[::-3]
s[-1::-3]
s[:0:-3]
s[-1:0:-3]
Review: String Slicing
'''

#4
'''
Suppose s is assigned as follows:

s = 'foobar'
All of the following expressions produce the same 
result except one. Which one?

s[::-5]

s[::5]

s[::-1][-1] + s[len(s)-1]

s[::-1][::-5]

s[0] + s[-1]


Yeah, these are kind of crazy. Just pick the indexing and slicing syntax apart one piece at a time.

When s is 'foobar', all of these answers produce the string 'fr':

s[0] + s[-1]
s[0] is the first character, 'f'.
s[-1] is the last character, 'r'.
s[::5]
[::5] specifies every fifth character, starting at the beginning and proceeding to the end (because the first two indices are allowed to default). Thus, the result is the first character, 'f', followed by the sixth character, 'r'.
s[::-1][-1] + s[len(s)-1]
s[::-1] reverses the string, so it equals 'raboof'. The added [-1] index specifies the last character of that string, 'f'.
s[len(s)-1] is the same as s[-1]—the last character of the original string, 'r'.
s[::-1][::-5]
As above, s[::-1] is 'raboof'. [::-5] specifies every fifth character, starting at the end and proceeding to the beginning (remember that when the stride is negative, the first index defaults to the end of the string, and the second index to the beginning, rather than the other way around). Thus, this returns 'f', then 'r'.
The remaining answer, s[::-5], specifies every fifth character, starting at the end of the string and proceeding to the beginning. When s is 'foobar', that results in 'rf'.

Review: String Indexing, String Slicing
'''

#6
'''
Which of the following are true:


s[:] is s

Incorrect

s[:] == s

Correct

s[::-1][::-1] == s

Correct

s[::-1][::-1] is s


s[:] creates an actual reference to the original string s. Thus, not only are s and s[:] equal, they have the same id() as well:

>>> s = 'foo'
>>> id(s)
60155776
>>> id(s[:])
60155776
s[::-1] reverses s, but creates a reference to a new object. An additional [::-1] slice reverses it again, so it is equal to the original s. But it is not the same object:

>>> s = 'foo'
>>> id(s)
60155776
>>> id(s[::-1][::-1])
63665824
Review: String Slicing
'''

#7
'''
Write the code for a Python function greet(person) that returns the string 'Hello, my name is <name>.', with person inserted in place of <name>.

Use an f-string to perform the variable interpolation:

def greet(person):
    return f"Hello,my name is {name}"
Incorrect
Return value should include {person}.

This is what we expected to see:
def greet(person):
    return f'Hello, my name is {person}.'

An f-string looks like an ordinary string, but it is 
prefixed with f or F. Interpolated variables in an 
f-string are enclosed in curly braces.
'''

#8
'''
What is the output from this print() function call:

print(
    '$100 $200 $300'.count('$'),
    '$100 $200 $300'.count('$', 5, 10),
    '$100 $200 $300'.count('$', 5)
)

3 2 1


3 1 2

Correct

3 1 1


3 1 0


str.count() counts occurrences of the given substring 
within the specified string.

The second and third parameters indicate 
<start> and <end> values, interpreted as for string 
slicing: the method applies to the portion of the 
string beginning with character position <start>, 
up to but not including <end>.

Review: Built-in String Methods
'''

#9
'''
Suppose s is assigned as follows:

s = 'foo-bar-baz'
 Which of the following expressions evaluates to a string equal to s:

'-'.join(s.split('-'))

Correct

s.strip('-')

Incorrect

s.center(15)


'-'.join(s.partition('-'))

Incorrect

s.upper().lower()

Correct

These expressions return s unchanged:

'-'.join(s.split('-'))
.split() and .join() are complementary methods. One reverses the effect of the other.
s.upper().lower()
.upper() returns a string contianing the upercase variants of all characters in the original string, or "FOO-BAR-BAZ" in this case. Then .lower() returns the string with lowercase variants of all characters, which is "foo-bar-baz" and is equal to s.
s.strip('-')
.strip() only removes leading and trailing characters. Since all the '-' characters are in the interior of s, none are removed in this case.
These expressions do not return a string equal to s:

'-'.join(s.partition('-'))
Unlike .split(), .partition() includes the separator character in the list it returns. The expression you’d need to join the list back together and obtain s again is ''.join(s.partition('-')).
s.center(15)
s.center() would return s unchanged if the field width specified were less than or equal to len(s). But it isn’t in this case.
Review: Built-in String Methods
'''

#10
'''
You want to create a bytes object consisting of five null (0x00) bytes. All of the following will work except one. Select the one that doesn’t work:


bytes(0, 0, 0, 0, 0)

Incorrect

bytes(5)

Incorrect

bytes('\x00\x00\x00\x00\x00', 'utf-8')


bytes([0] * 5)


As arguments, bytes() takes an integer, a string and an encoding, or an iterable. But not multiple integers.

Review: Defining a bytes Object With the Built-in bytes() Function
'''

print(bytes(5))

#11
print(list((b'abcde' + 'fghi')[3:6]))
# print(list((b'abcde' + 'fghi')[3:6]))
#TypeError: can't concat str to bytes

'''
What is the result of the following statement:

list((b'abcde' + 'fghi')[3:6])

[100, 101, 102]


[b'd', b'e', b'f']


['d', 'e', 'f']


It raises an exception

Correct

b'def'


The error lies in the expression (b'abcde' + 'fghi').

You can concatenate two bytes objects with the + operator, but not a bytes object and string:

>>> list((b'abcde' + 'fghi')[3:6])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't concat str to bytes
Review: Operations on bytes Objects
'''

#12
'''
A bytes object is immutable. If you want a binary sequence that can be modified, you should use a bytearray.

Is it possible to create a bytearray object directly from a bytes object, as shown below:

array_of_bytes = bytearray(b'15\x80a#')

No


Yes

Correct

You can also create a bytearray object with the bytearray() function, passing an integer, a string and an encoding, or an iterable.

But there is no built-in syntax for defining a bytearray object, similar to the b'' syntax for a bytes object.

Review: bytearray Objects
'''

#13
'''

'''