'''
Coroutines: Algorithms_ Memoization and Dynamic Programming(1080P_HD)

yield forms an expression that allows data to be sent into the generator (see footnote 3)

Here is an example, take note of the received variable, which will point to the data that is sent to the generator:

def bank_account(deposited, interest_rate):
    while True:
        calculated_interest = interest_rate * deposited 
        received = yield calculated_interest
        if received:
            deposited += received


>>> my_account = bank_account(1000, .05)
First, we must queue up the generator with the builtin function, next. It will call the appropriate next or __next__ method, depending on the version of Python you are using:

>>> first_year_interest = next(my_account)
>>> first_year_interest
50.0
And now we can send data into the generator. (Sending None is the same as calling next.) :

>>> next_year_interest = my_account.send(first_year_interest + 1000)
>>> next_year_interest
102.5
Cooperative Delegation to Sub-Coroutine with yield from
Now, recall that yield from is available in Python 3. This allows us to delegate coroutines to a subcoroutine:


def money_manager(expected_rate):
    # must receive deposited value from .send():
    under_management = yield                   # yield None to start.
    while True:
        try:
            additional_investment = yield expected_rate * under_management 
            if additional_investment:
                under_management += additional_investment
        except GeneratorExit:
            #TODO: write function to send unclaimed funds to state
            raise
        finally:
            #TODO: write function to mail tax info to client
        

def investment_account(deposited, manager):
    #very simple model of an investment account that delegates to a manager
    # must queue up manager:
    next(manager)      # <- same as manager.send(None)
    # This is where we send the initial deposit to the manager:
    manager.send(deposited)
    try:
        yield from manager
    except GeneratorExit:
        return manager.close()  # delegate?
And now we can delegate functionality to a sub-generator and it can be used by a generator just as above:

my_manager = money_manager(.06)
my_account = investment_account(1000, my_manager)
first_year_return = next(my_account) # -> 60.0
Now simulate adding another 1,000 to the account plus the return on the account (60.0):

next_year_return = my_account.send(first_year_return + 1000)
next_year_return # 123.6
You can read more about the precise semantics of yield from in PEP 380.

Other Methods: close and throw
The close method raises GeneratorExit at the point the function execution was frozen. This will also be called by __del__ so you can put any cleanup code where you handle the GeneratorExit:

my_account.close()
You can also throw an exception which can be handled in the generator or propagated back to the user:

import sys
try:
    raise ValueError
except:
    my_manager.throw(*sys.exc_info())
Raises:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
  File "<stdin>", line 6, in money_manager
  File "<stdin>", line 2, in <module>
ValueError
Conclusion
I believe I have covered all aspects of the following question:

What does the yield keyword do in Python?

It turns out that yield does a lot. I'm sure I could add even more thorough examples to this. If you want more or have some constructive criticism, let me know by commenting below.

Appendix:
Critique of the Top/Accepted Answer**
It is confused on what makes an iterable, just using a list as an example. See my references above, but in summary: an iterable has an __iter__ method returning an iterator. An iterator provides a .next (Python 2 or .__next__ (Python 3) method, which is implicitly called by for loops until it raises StopIteration, and once it does, it will continue to do so.
It then uses a generator expression to describe what a generator is. Since a generator is simply a convenient way to create an iterator, it only confuses the matter, and we still have not yet gotten to the yield part.
In Controlling a generator exhaustion he calls the .next method, when instead he should use the builtin function, next. It would be an appropriate layer of indirection, because his code does not work in Python 3.
Itertools? This was not relevant to what yield does at all.
No discussion of the methods that yield provides along with the new functionality yield from in Python 3. The top/accepted answer is a very incomplete answer.
Critique of answer suggesting yield in a generator expression or comprehension.
The grammar currently allows any expression in a list comprehension.

expr_stmt: testlist_star_expr (annassign | augassign (yield_expr|testlist) |
                     ('=' (yield_expr|testlist_star_expr))*)
...
yield_expr: 'yield' [yield_arg]
yield_arg: 'from' test | testlist

rite a generic function chainer
Write a generic function chainer that takes a starting value, and an array of functions to execute on it (array of symbols for Ruby).

The input for each function is the output of the previous function (except the first function, which takes the starting value as its input). Return the final value after execution is complete.


'''

def bank_account(deposited, interest_rate):
    while True:
        calculated_interest = interest_rate * deposited
        received = yield calculated_interest
        if received:
            deposited += received

my_account = bank_account(1000, .05)


first_year_interest = next(my_account)
print(first_year_interest)

next_year_interest = my_account.send(first_year_interest + 1000)
print(next_year_interest)





def investment_account(deposited, manager):
    '''very simple model of an investment account that delegates to a manager'''
    # must queue up manager:
    next(manager)      # <- same as manager.send(None)
    # This is where we send the initial deposit to the manager:
    manager.send(deposited)
    try:
        yield from manager
    except GeneratorExit:
        return manager.close()  # delegate?