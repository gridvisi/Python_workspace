'''
https://www.codewars.com/kata/5a793fdbfd8c06d07f0000d5/train/python

solve("3(ab)") = "ababab"     -- because "ab" repeats 3 times
solve("2(a3(b))" = "abbbabbb" -- because "a3(b)" == "abbb", which repeats twice.
Given a string, return the expansion of that string.

Input will consist of only lowercase letters and numbers (1 to 9) in valid parenthesis.
There will be no letters or numbers after the last closing parenthesis.

Test.it("Basic tests")
Test.assert_equals(solve("3(ab)"),"ababab")
Test.assert_equals(solve("2(a3(b))"),"abbbabbb")
Test.assert_equals(solve("3(b(2(c)))"),"bccbccbcc")
Test.assert_equals(solve("k(a3(b(a2(c))))"),"kabaccbaccbacc")
'''
from collections import deque

# -*- coding: utf-8 -*-


class Stack():

    def __init__(self):
        self.items = list()

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack.items)
    print(stack.peek())
    print(stack.isEmpty())

def solve(st):
    cal = deque()
    ans = ''
    cal = []
    for i in st:
        cal.append(i)
        if i == ")":
            cal.pop()
            ans += cal.pop(-1) #cal[-1]
            if cal[-1] == '(':
                cal.pop()
                ans *= cal[-1]

    pass