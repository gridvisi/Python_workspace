'''
https://www.geeksforgeeks.org/types-of-recursions/

What is Recursion?
The process in which a function calls itself directly or indirectly is called
recursion and the corresponding function is called a recursive function. Using
recursive algorithm, certain problems can be solved quite easily.
Examples of such problems are Towers of Hanoi (TOH),

Inorder/Preorder/Postorder Tree Traversals, DFS of Graph, etc.

Types of Recursions:
Recursion are mainly of two types depending on whether a function calls itself
from within itself or more than one function call one another mutually.

The first one is called direct recursion and another one is called indirect recursion.
Thus, the two types of recursion are:

1. Direct Recursion: These can be further categorized into four types:

Tail Recursion: If a recursive function calling itself and that recursive
call is the last statement in the function then it’s known as Tail Recursion.
After that call the recursive function performs nothing.

The function has to process or perform any operation at the time of calling and it
does nothing at returning time.
Example:

什么是递归？
一个函数直接或间接调用自己的过程被称为递归，相应的函数被称为递归函数。使用递归算法，某些问题可以很
容易地得到解决。这类问题的例子有：河内塔（TOH），Inorder/Preorder/Postorder树的遍历，图的DFS，
等等。

递归的类型。
递归主要有两种类型，取决于一个函数是在自己内部调用自己还是多个函数相互调用。第一种被称为直接递归，
另一种被称为间接递归。因此，两种类型的递归是。

1. 直接递归。这些可以进一步分为四种类型。

尾部递归。如果一个递归函数调用自己，并且该递归调用是该函数的最后一条语句，那么它就被称为尾部递归。
在这个调用之后，递归函数不执行任何操作。该函数在调用时必须处理或执行任何操作，在返回时不做任何事情。
例子。
'''


# Code Showing Tail Recursion

# Recursion function
def fun(n):
    if (n > 0):
        print(n, end=" ")
        # Last statement in the function
        fun(n - 1)

# Driver Code
x = 3
fun(x)

# This code is contributed by Shubhamsingh10

'''
Time Complexity For Tail Recursion : O(n) 
Space Complexity For Tail Recursion : O(n)
Note: Time & Space Complexity is given for this specific example. 
It may vary for another example.

Lets’s now converting Tail Recursion into Loop and compare each other 
in terms of Time & Space Complexity and decide which is more efficient.

尾部递归的时间复杂度: O(n) 
尾部递归的空间复杂度: O(n)
注：时间和空间复杂度是针对这个特定的例子给出的。对于另一个例子，它可能会有所不同。

现在让我们把尾部递归转换为循环，在时间和空间复杂度方面进行比较，并决定哪一个更有效。
'''


# Converting Tail Recursion into Loop
def fun(y):
    while (y > 0):
        print(y, end=" ")
        y -= 1


# Driver code
x = 3
fun(x)

# This Code is contributed by shivanisinghss2110

'''
me Complexity: O(n) 
Space Complexity: O(1)

Note: Time & Space Complexity is given for this specific example. It may vary for another example.
So it was seen that in case of loop the Space Complexity is O(1) so it was better to write code in loop instead of tail recursion in terms of Space Complexity which is more efficient than tail recursion.

Why space complexity is less in case of loop ?
Before explaining this I am assuming that you are familiar with the knowledge that’s how the data stored in main memory during execution of a program. In brief,when the program executes,the main memory divided into three parts. One part for code section, the second one is heap memory and another one is stack memory. Remember that the program can directly access only the stack memory, it can’t directly access the heap memory so we need the help of pointer to access the heap memory.

Let’s now understand why space complexity is less in case of loop ?
In case of loop when function “(void fun(int y))” executes there only one activation record created in stack memory(activation record created for only ‘y’ variable) so it takes only ‘one’ unit of memory inside stack so it’s space complexity is O(1) but in case of recursive function every time it calls itself for each call a separate activation record created in stack.So if there’s ‘n’ no of call then it takes ‘n’ unit of memory inside stack so it’s space complexity is O(n). 

Head Recursion: If a recursive function calling itself and that recursive call is 
the first statement in the function then it’s known as Head Recursion. 
There’s no statement, no operation before the call. The function doesn’t have to 
process or perform any operation at the time of calling and all operations are done 
at returning time.
Example:

我的复杂度。O(n) 
空间复杂度。O(1)

注：时间和空间的复杂性是针对这个特定的例子给出的。对于另一个例子，它可能会有所不同。
所以我们可以看到，在循环的情况下，空间复杂度是O(1)，所以就空间复杂度而言，最好是用循环来写代码，
而不是尾部递归，因为尾部递归比循环更有效。

为什么在循环的情况下空间复杂度较低？
在解释这个问题之前，我假设你已经熟悉了一些知识，即在程序执行过程中，数据是如何存储在主内存中的。
简而言之，当程序执行时，主内存被分为三部分。一部分是代码部分，第二部分是堆内存，另一部分是栈内存。
记住，程序只能直接访问堆内存，不能直接访问堆内存，所以我们需要指针的帮助来访问堆内存。

现在让我们来了解一下，为什么在循环的情况下，空间复杂度较低？
在循环的情况下，当函数"(void fun(int y)) "执行时，在堆栈内存中只创建了一条激活记录
（只为'y'变量创建激活记录），所以它只占用堆栈中的'一个'内存单位，所以它的空间复杂度是O(1)，
但在递归函数的情况下，它每次调用自己时都会在堆栈中创建一个单独的激活记录。

头部递归。如果一个递归函数调用自己，并且该递归调用是该函数的第一个语句，那么它就被称为头部递归。
在调用之前没有语句，没有操作。该函数在调用时不需要处理或执行任何操作，所有的操作都在返回时完成。
例子。

'''


# Python program showing Head Recursion
# Recursive function
def fun(n):
    if (n > 0):
        # First statement in the function
        fun(n - 1)
        print(n, end=" ")

# Driver code
x = 3
fun(x)

'''
Let’s understand the example by tracing tree of recursive function. That is how the calls are made and how the outputs are produced.



Time Complexity For Head Recursion: O(n) 
Space Complexity For Head Recursion: O(n)

Note: Time & Space Complexity is given for this specific example. It may vary for another example.
Note: Head recursion can’t easily convert into loop as Tail Recursion but it can. Let’s convert the above code into the loop.

让我们通过追踪递归函数的树来理解这个例子。这就是调用是如何进行的，输出是如何产生的。

头部递归的时间复杂度。O(n) 
头部递归的空间复杂度。O(n)

注：时间和空间复杂度是针对这个特定的例子给出的。对于另一个例子，它可能会有所不同。
注意：头部递归不能像尾部递归那样轻易地转换为循环，但它可以。让我们把上面的代码转换为循环。
'''


# Converting Head Recursion into Loop
# Recursive function
def fun(n):
    i = 1
    while (i <= n):
        print(i, end=" ")
        i += 1


# Driver code
x = 3
fun(x)

# This code is contributed by shivanisinghss2110

'''

Tree Recursion: To understand Tree Recursion let’s first understand Linear Recursion. If a recursive function calling itself for one time then it’s known as Linear Recursion. Otherwise if a recursive function calling itself for more than one time then it’s known as Tree Recursion.
Example:
Pseudo Code for linear recursion
fun(n)
{
    // some code
    if(n>0)
    {
        fun(n-1); // Calling itself only once
    }
    // some code
}
Program for tree recursion


Time Complexity For Tree Recursion: O(2^n) 
Space Complexity For Tree Recursion: O(n)
Note: Time & Space Complexity is given for this specific example. It may vary for another example.

Nested Recursion: In this recursion, a recursive function will pass the parameter as a recursive call. That means “recursion inside recursion”. Let see the example to understand this recursion.
Example:
'''


# C++ program to show Tree Recursion
# Recursive function
def fun(n):
    if (n > 0):
        print(n)

        # Calling once
        fun(n - 1)

        # Calling twice
        fun(n - 1)


# Driver code
fun(3)


# Python program to show Nested Recursion
def fun(n):
    if (n > 100):
        return n - 10

    # A recursive function passing parameter
    # as a recursive call or recursion inside
    # the recursion
    return fun(fun(n + 11))

# Driver code
r = fun(95)
print("", r)

# This code is contributed by shivanisinghss2110

'''
Let’s understand the example by tracing tree of recursive function. 
That is how the calls are made and how the outputs are produced.

2. Indirect Recursion: In this recursion, there may be more than one 
functions and they are calling one another in a circular manner.

From the above diagram fun(A) is calling for fun(B), fun(B) is calling 
for fun(C) and fun(C) is calling for fun(A) and thus it makes a cycle.
'''


# Python program to show Indirect Recursion
def funA(n):
    if (n > 0):
        print("", n, end='')

        # Fun(A) is calling fun(B)
        funB(n - 1)


def funB(n):
    if (n > 1):
        print("", n, end='')

        # Fun(B) is calling fun(A)
        funA(n // 2)


# Driver code
funA(20)
#Output: 20 19 9 8 4 3 1
# This code is contributed by shivanisinghss2110

'''
本文由AmiyaRanjanRout贡献。如果你喜欢GeeksforGeeks并想投稿，你也可以使用
write.geekforgeeks.org写一篇文章，或者将你的文章邮寄到review-team@geeksforgeeks.org.See，
让你的文章出现在GeeksforGeeks的主页上，并帮助其他Geeks。
 

读者请注意! 现在不要停止学习。通过DSA自学课程掌握所有重要的DSA概念，并以适合学生的价格成为行业的
准备者。 要完成从学习语言到DS Algo以及更多的准备工作，请参考完整的面试准备课程。

如果你想参加专家的现场课程，请参考为在职专业人士开设的DSA现场课程和为学生开设的竞争性编程现场课程。
'''