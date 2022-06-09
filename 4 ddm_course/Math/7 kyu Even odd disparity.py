'''
https://www.codewars.com/kata/59c62f1bdcc40560a2000060/train/python

Test.it("Basic tests")
Test.assert_equals(solve([0,1,2,3]),0)
Test.assert_equals(solve([0,1,2,3,'a','b']),0)
Test.assert_equals(solve([0, 15,'z',16,'m', 13, 14,'c', 9, 10, 13,'u', 4, 3]),0)
Test.assert_equals(solve([13, 6, 8, 15, 4, 8, 13]),1)
Test.assert_equals(solve([1,'a', 17, 8,'e', 3,'i', 12, 1]),-2)
'''

def solve(a):
    ans = [i%2 == 0 for i in a if not str(i).isalpha()]
    return ans.count(True) - ans.count(False)

a = [1,'a', 17, 8,'e', 3,'i', 12, 1]

#1st solution
def solve(a):
    return sum(1 if v % 2 == 0 else -1 for v in a if type(v) == int)
print(solve(a))

#isdigit()、isalpha()、isalnum() 三个函数的区别和注意点
'''
python关于 isdigit() 内置函数的官方定义：
S.isdigit() -> bool        
        Return True if all characters in S are digits
        and there is at least one character in S, False otherwise.
翻译：
S.isdigit()返回的是布尔值：True False
S中至少有一个字符且如果S中的所有字符都是数字，那么返回结果就是True；否则，就返回False
'''
print()
S1 = '12345'       #纯数字
S2 = '①②'        #带圈的数字
S3 = '汉字'        #汉字
S4 = '%#￥'        #特殊符号

print(S1.isdigit())
print(S2.isdigit())
print(S3.isdigit())
print(S4.isdigit())

'''
isalpha() 内置函数的官方定义：
S.isalpha() -> bool        
        Return True if all characters in S are alphabetic
        and there is at least one character in S, False otherwise.
翻译：
S.isalpha()返回的是布尔值：True False
S中至少有一个字符且如果S中的所有字符都是字母，那么返回结果就是True；否则，就返回False
'''

S1 = 'abc汉字'     #汉字+字母
S2 = 'ab字134'     #包含数字
S3 = '*&&'         #特殊符号

print(S1.isalpha())
print(S2.isalpha())
print(S3.isalpha())


'''
 isalnum() 内置函数的官方定义：
S.isalnum() -> bool 
        Return True if all characters in S are alphanumeric
        and there is at least one character in S, False otherwise.
翻译：
S.isalnum()返回的是布尔值：True False
S中至少有一个字符且如果S中的所有字符都是字母数字，那么返回结果就是True；否则，就返回False
'''

S1 = 'abc汉字1'    #字母+汉字+数字
S2 = '①②③'      #带圈的数字
S3 = '%……&'       #特殊符号

print(S1.isalnum())
print(S2.isalnum())
print(S3.isalnum())
