'''
https://brilliant.org/daily-problems/liars-paradox/

All the statements below this one are false.
All the statements below this one are false.
All the statements below this one are false.
None of the statements above this one are true.
None of the statements above this one are true.
None of the statements above this one are true.
'''

s1,s2,s3,s4,s5,s6 = [True] * 6
print(s1,s2,s3,s4,s5)

def liars_paradox(s1,s2,s3,s4,s5,s6):
    if s1 == True:
        s2, s3, s4, s5,s6 = [not(i) for i in [s2, s3, s4, s5,s6]]

    elif s2 == True:
        s3, s4, s5,s6 = [not(i) for i in [s3, s4, s5,s6]]

    elif s3 == True:
        s4, s5,s6 = [not (i) for i in [s4, s5,s6]]

    elif s4 == True:
        s1, s2, s3 = [not(i) for i in [s1, s2, s3]]

    elif s5 == True:
        s1, s2, s3,s4 = [not(i) for i in [s1, s2, s3,s4]]

    elif s6 == True:
        s1, s2, s3, s4, s5 = [not (i) for i in [s1, s2, s3, s4,s5]]
    return s1,s2,s3,s4,s5,s6
#s1,s2,s3,s4,s5,s6 = True, False, False, False, False, False
print(liars_paradox(s1,s2,s3,s4,s5,s6))

# Good solution
# itertools
from itertools import product

for bools in product((True, False), repeat=6):
    for i in range(len(bools)):
        statement = not any(bools[i + 1:]) if i < 3 else not any(bools[:i])
        if statement != bools[i]:
            break
    else:
        print(bools)

'''
Let's dissect each of these statements from the top.

Suppose statement 1 is true. Then all the statements below it 
are false. 

This means all the statements below statement 2 are false, too, 
making statement 2 true. But this means that statement 1 is no 
longer true, a contradiction! So, statement 1 has to be false. 

This also means that at least one of the remaining 5 statements 
must be true.

Suppose statement 2 is true. Then all the statements below it are 
false. 

This means all the statements below statement 3 are false, too, 
making statement 3 true. But this means that statement 2 is no 
longer true, a contradiction! So, statement 2 has to be false.

Suppose statement 3 is true. Then all the statements below it are 
false. Since there's 1 true statement above statement 4, statements 
4 through 6 are indeed false.

Now, suppose statement 3 is false. This means that statement 4 must 
be true. Subsequently, the latter two statements must be false.

In summary, exactly one of statement 3 and statement 4 must be true, 
and the remaining statements must be false.

The largest number of statements that can be simultaneously true 
is 1
​	
让我们从头剖析一下这些说法。

假设陈述1是真的。那么它下面的所有陈述都是假的。这意味着陈述2下面的所有陈述也都
是假的，使得陈述2是真的。但是，这意味着语句1不再是真，是一个矛盾！

所以，语句1必须是假的。所以，语句1必须是假的。这也意味着剩下的5个语句中至少有一
个必须是真的。

假设语句2为真。那么它下面的所有语句都是假的。这意味着陈述3下面的所有陈述也都是假
的，使得陈述3为真。但这意味着语句2不再是真，是矛盾的！所以，语句2必须是假的。

所以，语句2必须是假的。

假设语句3为真。那么它下面的所有语句都是假的。由于语句4上面有一个真语句，所以语句
4到6确实是假的。

现在，假设语句3是假的。这意味着陈述4一定是真的。随后，后两个语句一定是假的。

综上所述，陈述3和陈述4中恰好有一个是真，其余的陈述一定是假。

最多可以同时为真的语句数量为1。
1
	
 .
'''
