'''
https://www.geeksforgeeks.org/tail-recursion/

What is tail recursion?
A recursive function is tail recursive when a recursive call is the
last thing executed by the function.

For example the following C++ function print() is tail recursive.
'''


# An example of tail recursive function
def prints(n):
    if (n < 0):
        return
    print(str(n), end=' ')

    # The last executed statement is recursive call
    prints(n - 1)

    # This code is contributed by Pratham76
    # improved by ashish2021

'''
Why do we care? 
The tail recursive functions considered better than non tail recursive functions as tail-recursion can be optimized by the compiler. Compilers usually execute recursive procedures by using a stack. This stack consists of all the pertinent information, including the parameter values, for each recursive call. When a procedure is called, its information is pushed onto a stack, and when the function terminates the information is popped out of the stack. Thus for the non-tail-recursive functions, the stack depth (maximum amount of stack space used at any time during compilation) is more. The idea used by compilers to optimize tail-recursive functions is simple, since the recursive call is the last statement, there is nothing left to do in the current function, so saving the current function’s stack frame is of no use (See this for more details).

Can a non-tail recursive function be written as tail-recursive to optimize it? 
Consider the following function to calculate the factorial of n. It is a non-tail-recursive function. Although it looks like a tail recursive at first look. If we take a closer look, we can see that the value returned by fact(n-1) is used in fact(n), so the call to fact(n-1) is not the last thing done by fact(n) 


我们为什么关心这个问题？
尾部递归函数被认为比非尾部递归函数更好，因为尾部递归可以被编译器优化。编译器通常通过使用
一个堆栈来执行递归程序。这个堆栈由所有相关的信息组成，包括每个递归调用的参数值。当一个程序
被调用时，它的信息被推到堆栈中，当函数终止时，信息被从堆栈中弹出。因此，对于非尾部递归函数
来说，堆栈深度（编译过程中任何时候使用的最大堆栈空间）是更多的。编译器用来优化尾部递归函数
的想法很简单，因为递归调用是最后一条语句，在当前函数中已经没有什么可做的了，所以保存当前函
数的堆栈框架是没有用的（详情见此）。

一个非尾部递归的函数可以写成尾部递归来优化它吗？
考虑一下下面这个计算n的阶乘的函数，它是一个非尾递归函数。虽然它乍一看像一个尾部递归。如果我
们仔细观察，我们可以看到 fact(n-1) 返回的值被用在 fact(n) 中，所以对 fact(n-1) 的调
用并不是 fact(n) 最后做的事情。

'''


# A NON-tail-recursive function.
# The function is not tail
# recursive because the value
# returned by fact(n-1) is used
# in fact(n) and call to fact(n-1)
# is not the last thing done by
# fact(n)
def fact(n):
    if (n == 0):
        return 1

    return n * fact(n - 1)


# Driver program to test
# above function
print(fact(5))
# This code is contributed by Smitha.

'''
Let’s understand the example by tracing tree of recursive 
function. That is how the calls are made and how the outputs 
are produced.

Time Complexity For Tail Recursion : O(n) 
Space Complexity For Tail Recursion : O(n)
Note: Time & Space Complexity is given for this specific 
example. It may vary for another example.

Lets’s now converting Tail Recursion into Loop and compare 
each other in terms of Time & Space Complexity and decide 
which is more efficient.

让我们通过追踪递归函数的树来理解这个例子。这就是调用是如何进行的，输出是如何产生的。

尾部递归的时间复杂度: O(n) 
尾部递归的空间复杂度。O(n)
注：时间和空间复杂度是针对这个特定的例子给出的。对于另一个例子，它可能会有所不同。

现在让我们把尾部递归转换为循环，在时间和空间复杂度方面进行比较，并决定哪一个更有效。
'''

#https://www.geeksforgeeks.org/tail-recursion/#:~:text=%23%20A%20tail%20recursive,by%20Ujwal%2C%20ashish2021

# A tail recursive function
# to calculate factorial
def fact(n, a=1):
    if (n == 1):
        return a

    return fact(n - 1, n * a)


# Driver program to test
#  above function
print(fact(5))

# This code is contributed
# by Smitha
# improved by Ujwal, ashish2021