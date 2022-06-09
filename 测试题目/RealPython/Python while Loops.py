# https://realpython.com/quizzes/python-while-loop/viewer/

#1
'''
A while loop in Python is used for what type of iteration?
discriminant
indefinite
definite
indeterminate

A while loop implements indefinite iteration, where the
number of times the loop will be executed is not specified
explicitly in advance. (Indeterminate would probably be an
apt description of this type of iteration as well, but not
the term that is typically used.)

Definite iteration is implemented with the for loop in
Python (which is covered in the next tutorial in the
series).

Discriminant isn’t even an adjective, much less a
description of any type of iteration.

All right, that was easy. We’re just getting warmed up …

while循环实现了不确定的迭代，即循环的执行次数没有事先明确指定。
(不确定可能也是对这种类型的迭代的恰当描述，但不是通常使用的术语)。

确定的迭代是用Python中的for循环来实现的（这将在本系列的下一个教程
中讲述）。

判别甚至不是一个形容词，更不是对任何类型的迭代的描述。

好了，这很容易。我们刚刚开始热身 ...
'''


#2
'''
What is the output of the following code snippet:

d = {'foo': 1, 'bar': 2, 'baz': 3}
while d:
    print(d.popitem())
print('Done.')

Done.

('baz', 3)
('bar', 2)
('foo', 1)
Done.
Correct

foo
bar
baz

The snippet doesn’t generate any output.
The .popitem() method removes one key-value pair from d 
and returns 
it as a tuple. So the body of this while loop displays 
the contents of d as tuples.

Once the last key-value pair has been removed, d is empty and is falsy in Boolean context. The while loop then terminates and displays the line following the 
loop body.
'''

#3
'''
What is the output of this code snippet:

d = {'foo': 1, 'bar': 2, 'baz': 3}
while len(d) > 3:
    print(d.popitem())
print('Done.')

The snippet doesn’t generate any output.


('baz', 3)
('bar', 2)
('foo', 1)
Done.

foo
bar
baz

Done.
'''

#4
'''
What is the output of the following code snippet:

a = ['foo', 'bar', 'baz', 'qux', 'corge']
while a:
    if len(a) < 3:
        break
    print(a.pop())
print('Done.')

corge
qux
baz

The snippet doesn’t generate any output.


corge
qux
baz
bar
foo
Done.

corge
qux
baz
Done.
Correct

When no arguments are specified, a.pop() removes and 
returns the last item in a. So each time through the 
loop, the last item is displayed.

But when the loop contains fewer than three items, the 
break statement on line 4 is reached, and the loop is 
terminated. Execution then proceeds to the print() 
statement following the loop, on line 6.

Review: Interruption of Loop Iteration
'''

#5
'''
This code is identical to the code in the previous 
question except that the break statement is replaced 
by a continue statement:

a = ['foo', 'bar', 'baz', 'qux', 'corge']
while a:
    if len(a) < 3:
        continue
    print(a.pop())
print('Done.')
How does that change the behavior?


This code displays all the items in a.


The code prints the same list items as the loop in 
the previous question, but this loop never terminates.

Correct

This code doesn’t generate any output.


This code behaves identically to the code in the 
previous question.


As in the last example, each time through the loop the 
last list item is popped and displayed. 
Items 'corge', 'qux', and 'baz' are displayed as before.

In this case, though, when the list shrinks to fewer 
than three items, a continue statement is executed 
instead of a break statement. Instead of terminating 
the loop completely, execution jumps to the top of the 
loop and the while loop expression is re-evaluated. 
a is truthy because it is not empty, so the loop 
executes again.

When the if statement on line 3 is encountered, the 
length of a is still less than three, so the continue 
statement is executed again, and once again execution 
jumps to the top of the loop. a is still truthy, so the 
loop executes again. And so on, indefinitely.

This code generates the same output as the code in the 
previous question, but the loop never terminates after 
that. All list elements are printed in the same order 
as before, but there’s no “Done.” text printed at the 
end.

Review: Interruption of Loop Iteration
'''

#6
'''
Will the print() statement on line 5 be executed in this case:

a = ['foo', 'bar', 'baz', 'qux', 'corge']
while a:
    print(a.pop())
else:
    print('Done.')

Yes

Correct

No


The else clause of a while loop is executed if the loop terminates “by exaustion”, meaning it iterates until the condition becomes false. That occurs in this case, so the statement on line 5 will execute.

An else clause is not executed when a while loop is terminated prematurely with a break statement.

Review: The else clause
'''

#7
'''
Consider these while loop headers:

while True:
    …
 
a = ['foo', 'bar', 'baz', 'qux', 'corge']
while a:
    …
 
n = 100
while n > 0:
    …
 
while "0":
    …
Which one(s) initiate an infinite loop?


All of them.


None of them.


All but the last.


It depends on the code in the body of the loop.

Correct

It’s a bit of a trick question, but the best answer is that it depends on what happens in the body of the loop.

In general, the code in the loop body needs to modify one or more variables that appear in the loop’s controlling expression in such a way that the expression eventually becomes false. If not, virtually any while loop can become infinite.

But then, any loop can terminate if a break statement is executed, irrespective of the loop’s controlling expression.

Consider again the examples given:

while True:
    …
There’s no way to modify the controlling expression in this case. Unless a break statement is executed at some point, this loop will continue indefinitely. (Actually, there is another way. You could terminate a loop by raising an exception. Exceptions are covered more fully in an upcoming tutorial.)
a = ['foo', 'bar', 'baz', 'qux', 'corge']
while a:
    …
 
n = 100
while n > 0:
    …
In these cases, whether the loop terminates depends on if and how a and n are modified within the loop body.
while "0":
    …
"0" is truthy, and there’s no way to modify the controlling expression. A break statement could be used to break out of the loop.
Review: Infinite Loops
'''

#8
'''
s = ""

n = 5
while n > 0:
    n -= 1
    if (n % 2) == 0:
        continue

    a = ['foo', 'bar', 'baz']
    while a:
        s += str(n) + a.pop(0)
        if len(a) < 2:
            break
'''
s = ""

n = 5
while n > 0:
    n -= 1
    if (n % 2) == 0:
        continue
    print(n)
    a = ['foo', 'bar', 'baz']
    while a:
        s += str(n) + a.pop(0)
        if len(a) < 2:
            break
print(s)
'''
The continue on line 7 applies to the outer while loop; 
the break on line 13 applies to the inner while loop.

n is decremented straight away at the top of the outer 
loop, so during the body of the loop it effectively has 
successive values 4, 3, 2, 1, and 0. 

The continue is executed on the even values, so the inner 
while loop only occurs when n is 3 and 1.

Inside the inner while loop, a.pop(0) removes the first item of a. Once this has occurred twice, yielding 'foo' and 'bar', a has fewer than two items, and the break terminates the inner loop.

Thus, the values concatenated onto s are, in turn, 3foo, 3bar, 1foo, and 1bar.
'''

#9
'''
Assume a non-empty list a. Write a one-line while loop that uses the list.pop() method to remove all the values from a.

while a:
    a.pop()
a.pop()
Incorrect
IndexError: pop index out of range

This is what we expected to see:
while a: a.pop()

Although this works, it is unlikely you’d clear a list this way. Either of these is much more straightforward:

a.clear()
 
a = []
Also, remember these points:

Only a simple statement may occur on the same line as while.
PEP 8 discourages it.
Review: One-Line while Loops
'''