'''
https://www.codewars.com/kata/5f7c38eb54307c002a2b8cc8/train/python

@test.describe("remove parentheses")
def tests():
    @test.it("basic tests")
    def basic():
        test.assert_equals(remove_parentheses("example(unwanted thing)example"), "exampleexample")
        test.assert_equals(remove_parentheses("example (unwanted thing) example"), "example  example")
        test.assert_equals(remove_parentheses("a (bc d)e"), "a e")
        test.assert_equals(remove_parentheses("a(b(c))"), "a")
        test.assert_equals(remove_parentheses("hello example (words(more words) here) something"), "hello example  something")
        test.assert_equals(remove_parentheses("(first group) (second group) (third group)"), "  ")
'''
s = "a(b(c))"  #, "a")
print(s[7:])
 #" "


from collections import deque
def remove_parentheses(s):
    flag, opt = 0, ""
    for i in s:
        if i == '(':
            flag += 1
        if not flag:
            opt += i
        if i == ')':
            flag -= 1

    return opt

s = "(first group) (second group) (third group)"
s = "hello example (words(more words) here) something"


def remove_parentheses(s):
    lvl,out = 0,[]
    for c in s:
        lvl += c=='('
        if not lvl: out.append(c)
        lvl -= c==')'
    return ''.join(out)
print(remove_parentheses(s))


import re
def remove_parentheses(s):
    while (t := re.sub(r'\([^()]*\)', '', s)) != s:
        s = t
    return s

def remove_parentheses(s):
    ret, count = "", 0
    for letter in s:
        if letter == "(": count +=1
        elif letter == ")": count -=1
        elif count == 0: ret += letter
    return ret


# Recurtion
def remove_parentheses(s,left='',right=''):
    rem = [i for i,e in enumerate(s) if e == '(' or e == ')']
    #print(s[rem[0]],s[rem[-1]],len(s)-1)
    print(left,right)
    left += ''.join(s[:rem[0]])
    right = ''.join(s[rem[-1]+1:]) + right
    s = s[rem[0]:rem[-1]+1]
    if '(' in s and ')' in s:
        return remove_parentheses(s,left,right)
    return left+right



from collections import deque
def remove_parentheses(s):
    st, nd = [], []
    inside = deque()
    rem = deque()
    for i,e in enumerate(s):
        rem.append(e)
        if e == '(': st.append(i)
        if e == ')': nd.append(i)
        print('2',st,nd)
        if st and nd:
            front = nd[-1]
            print('st,front',rem,st,front)
            while front > st[-1] and rem:
                x = rem.pop()
                if x not in ['(', ')']:
                    inside.appendleft(x)
                print(inside,front, rem)
                front -= 1
        #print('rem',rem,temp)
    return rem ,''.join(inside)


class Stack():   #定义类
	def __init__(self):  #产生一个空的容器
		self.__list = []

	def push(self, item):  #入栈
		self.__list.append(item)

	def pop(self):  #出栈
		return self.__list.pop()

	def speek(self):  #返回栈顶元素
		return self.__list[-1]

	def is_empty(self):  #判断是否已为空
		return not self.__list

	def size(self):  #返回栈中元素个数
		return len(self.__list)