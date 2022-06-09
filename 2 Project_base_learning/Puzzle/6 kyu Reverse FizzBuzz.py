'''
https://www.codewars.com/kata/5a622f5f85bef7a9e90009e2/train/python

reverse_fizzbuzz("1 2 Fizz 4 Buzz")        -->  [1, 2, 3, 4, 5]
reverse_fizzbuzz("Fizz 688 689 FizzBuzz")  -->  [687, 688, 689, 690]
reverse_fizzbuzz("Fizz Buzz")              -->  [9, 10]

FizzBuzz往往是人们最先学会的编程难题之一。现在用反向FizzBuzz来撤销它吧!

写一个函数，接受一个字符串，这将永远是FizzBuzz的有效部分。你的函数必须返回一个包含数字的数组，
以便生成FizzBuzz的给定部分。

注释:
如果序列可以在FizzBuzz中出现多次，返回生成序列的第一个实例的数字。
序列中的所有数字都将大于零。
你永远不会收到一个空的序列。


test.describe("Sample tests")

test.assert_equals(reverse_fizzbuzz("1 2 Fizz 4 Buzz"), [1, 2, 3, 4, 5])
test.assert_equals(reverse_fizzbuzz("Fizz 688 689 FizzBuzz"), [687, 688, 689, 690])
test.assert_equals(reverse_fizzbuzz("Fizz Buzz"), [9, 10])
'''
print(eval("688 + 689"))

#12th solution by ericlee
def reverse_fizzbuzz(string):
    if string == "Fizz Buzz":return [9,10]
    if string == "Buzz Fizz":return [5,6]
    if string == 'Fizz':return [3]
    if string == 'Buzz':return [5]
    if string == "FizzBuzz":return [15]

    ans = []
    st = [int(i) if not i.isalpha() else 0 for i in string.split(' ')]
    bench = [[i,c] for i,c in enumerate(st) if c != 0]
    print(bench[0][1] - bench[0][0])
    ans = [i for i in range(bench[0][1] - bench[0][0],bench[0][1] - bench[0][0]+len(st),1)]

    return ans
string = "Fizz 688 689 FizzBuzz"
string = "1 2 Fizz 4 Buzz"
string = "Fizz 6433 6434 FizzBuzz 6436 6437 Fizz 6439 Buzz Fizz 6442 6443 Fizz Buzz 6446 Fizz 6448 6449 FizzBuzz 6451 6452 Fizz 6454 Buzz Fizz"
print(reverse_fizzbuzz(string))

#1st solution
def reverse_fizzbuzz(s):
    if s == 'Fizz': return [3]
    if s == 'Buzz': return [5]
    if s == 'Fizz Buzz': return [9, 10]
    if s == 'Buzz Fizz': return [5, 6]
    if s == 'FizzBuzz': return [15]
    s = s.split()
    for i in range(len(s)):
        if s[i].isdigit():
            start = int(s[i]) - i
            return list(range(start, start + len(s)))

def reverse_fizzbuzz(string):
    st = [int(i) if not i.isalpha() else 0 for i in string.split(' ')]
    print(st)
    for i,c in enumerate(st):
        print(i,c)
        if c == 0 and 0 < i <= len(st)-1:
            c += 5
        else:
            c = 5
    return st


def reverse_fizzbuzz(string):
    if string == "Fizz Buzz":return [9,10]
    ans = []
    st = [int(i) if not i.isalpha() else 0 for i in string.split(' ')]
    print(st)
    for i,c in enumerate(st):
        if c != 0:
            ans.append(c)
        elif c == 0:
            if i == 0:
                ans.append(st[i+1] - 1)
            elif i <= len(st)-1:
                ans.append(st[i-1] +1)
    return ans