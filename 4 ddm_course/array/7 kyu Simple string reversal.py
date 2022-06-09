# https://blog.csdn.net/sibyl_pisces/article/details/78423203

'''
https://www.codewars.com/kata/5a71939d373c2e634200008e/train/python

solve("our code") = "edo cruo"
-- Normal reversal without spaces is "edocruo".
-- However, there is a space at index 3, so the string becomes "edo cruo"

solve("your code rocks") = "skco redo cruoy".
solve("codewars") = "srawedoc"

Test.it("Basic tests")
Test.assert_equals(solve("codewars"),"srawedoc")
Test.assert_equals(solve("your code"),"edoc ruoy")
Test.assert_equals(solve("your code rocks"),"skco redo cruoy")
Test.assert_equals(solve("i love codewars"),"s rawe docevoli")
'''

s ="your code rocks"

def solve(s):
    sl = [i for i,e in enumerate(s) if e ==' ']
    print(list(''.join(s[::-1].split(' '))))
    ans = list(''.join(s[::-1].split(' ')))
    for i in sl:
        #ans = list(''.join(s[::-1].split(' '))).insert(i, ' ') # Not good!!!
        ans.insert(i,' ')
    return ''.join(ans)
print(solve(s))

# think it over : why follow code is not good?
s = [s.index(i) for i in s]

#1st solution

s ="your code rocks"
s = "i love codewars"
def solve(s):
    #it = iter(reversed(s.replace(' ','')))
    it = reversed(s.replace(' ', ''))
    return ''.join(c if c == ' ' else next(it) for c in s)
print(solve(s))

# 为何reversed不需要 iter() 下面列子需要iter() ？
st = iter('helloworld')
#st = 'hello world'
end = 'hello world'
#print(''.join(c if c == ' ' else next(st) for c in end))
print([c if c == ' ' else next(st) for c in end])
# 解释原因：
# 1、当c == ' '时，next(st) st停留在字母'o'，
# 2、变量c再取下一个值 c==p,条件判断p不是空格，执行next(st)，所以生成字母'o'后的' '空格
# 3、变量c == 'd' 时，nextst 计步器因为步骤2轮空1次，nextst慢一步到'l'
# key point: ' '空格后面又紧跟' ',是next(st)生成的空格，前一个空格是变量c，后一个空格是next(it)

# 尝试修改end = 'hello worlde' 时，输出为：
# ['h', 'e', 'l', 'l', 'o', ' ', ' ', 'w', 'o', 'r', 'l', 'd']

# 或 st = iter('helloworld')
# ['h', 'e', 'l', 'l', 'o', ' ', ' ', 'w', 'o', 'r', 'l', 'd']

s = "hello"
print(list(s))
s_iter = reversed(s)
print(s_iter)
print(reversed(s).__next__())