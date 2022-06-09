'''
Haskell 有一些处理列表的有用函数。

$ ghci
GHCi，7.6.3版：http://www.haskell.org/ghc/:?寻求帮助。
λ头[1,2,3,4,5]
1
λ尾数[1,2,3,4,5]
[2,3,4,5]
λ init [1,2,3,4,5]
[1,2,3,4]
λ最后[1,2,3,4,5]
5
你的工作是在你给定的语言中实现这些函数。确保它不会编辑数组，那会导致问题。这里有一个小抄。

| HEAD | <----------- TAIL ------------> |。
[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
<----------- INIT ------------> | LAST | <-----------

头 [x] = x
尾部[x]=[]
init [x] = []
最后[x]=x
下面是我希望在你的语言中调用函数的方式。

Head([1,2,3,4,5]) => 1
尾数([1,2,3,4,5]) => [2,3,4,5]
大多数测试由100个随机生成的数组组成，每个数组有4个测试，每个操作一个。总共有400个测试。不会给出空数组。
Haskell 有 QuickCheck 测试

基礎框架框架基本語言功能列表數據結構


Haskell has some useful functions for dealing with lists:

$ ghci
GHCi, version 7.6.3: http://www.haskell.org/ghc/  :? for help
λ head [1,2,3,4,5]
1
λ tail [1,2,3,4,5]
[2,3,4,5]
λ init [1,2,3,4,5]
[1,2,3,4]
λ last [1,2,3,4,5]
5
Your job is to implement these functions in your given language. Make sure it doesn't edit the array;
that would cause problems! Here's a cheat sheet:

| HEAD | <----------- TAIL ------------> |
[  1,  2,  3,  4,  5,  6,  7,  8,  9,  10]
| <----------- INIT ------------> | LAST |

head [x] = x
tail [x] = []
init [x] = []
last [x] = x
Here's how I expect the functions to be called in your language:

head([1,2,3,4,5]) => 1
tail([1,2,3,4,5]) => [2,3,4,5]
Most tests consist of 100 randomly generated arrays, each with four tests, one for each operation. There are 400 tests overall. No empty arrays will be given. Haskell has QuickCheck tests

FUNDAMENTALSARRAYSRANGESBASIC LANGUAGE FEATURESLISTSDATA STRUCTURES

| HEAD | <----------- TAIL ------------> |
[  1,  2,  3,  4,  5,  6,  7,  8,  9,  10]
| <----------- INIT ------------> | LAST |

head [x] = x
tail [x] = []
init [x] = []
last [x] = x

test.assert_equals( head([5,1]), 5 );
test.assert_equals( tail([1]), [] );
test.assert_equals( init([1,5,7,9]), [1,5,7] );
test.assert_equals( last([7,2]), 2 );
'''

def head(x):
    return x[0]

def tail(x):
    return x[1:]

def init(x):
    return x[:-1]

def last(x):
    return x[-1]

x = [  1,  2,  3,  4,  5,  6,  7,  8,  9,  10]
print(head(x),tail(x),init(x),last(x))