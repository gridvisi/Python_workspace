'''
https://www.codewars.com/kata/5e67ce1b32b02d0028148094/train/python

@test.describe('Sample Tests')
def sample_tests():

	def OR(A, B): return A or B
	def XOR(A, B): return A ^ B
	def NOR(A, B): return not(A or B)
	def AND(A, B): return A and B
	def NAND(A, B): return not (A and B)
	def FALSE(A, B, C, D): return False
	def TRUE(A, B, C): return True
	def NOT(A): return not A
	anonymous_function = lambda A, B, C: A and B or not C

	@test.it('classic functions')
	def testing_classic_functions():
		test.assert_equals(truth_table(AND), 'A B\t\tAND(A,B)\n\n0 0\t\t0\n0 1\t\t0\n1 0\t\t0\n1 1\t\t1\n')
		test.assert_equals(truth_table(XOR), 'A B\t\tXOR(A,B)\n\n0 0\t\t0\n0 1\t\t1\n1 0\t\t1\n1 1\t\t0\n')
		test.assert_equals(truth_table(OR), 'A B\t\tOR(A,B)\n\n0 0\t\t0\n0 1\t\t1\n1 0\t\t1\n1 1\t\t1\n')
		test.assert_equals(truth_table(NOR), 'A B\t\tNOR(A,B)\n\n0 0\t\t1\n0 1\t\t0\n1 0\t\t0\n1 1\t\t0\n')
		test.assert_equals(truth_table(NAND), 'A B\t\tNAND(A,B)\n\n0 0\t\t1\n0 1\t\t1\n1 0\t\t1\n1 1\t\t0\n')
		test.assert_equals(truth_table(NOT), 'A\t\tNOT(A)\n\n0\t\t1\n1\t\t0\n')
		test.assert_equals(truth_table(FALSE), 'A B C D\t\tFALSE(A,B,C,D)\n\n0 0 0 0\t\t0\n0 0 0 1\t\t0\n0 0 1 0\t\t0\n0 0 1 1\t\t0\n0 1 0 0\t\t0\n0 1 0 1\t\t0\n0 1 1 0\t\t0\n0 1 1 1\t\t0\n1 0 0 0\t\t0\n1 0 0 1\t\t0\n1 0 1 0\t\t0\n1 0 1 1\t\t0\n1 1 0 0\t\t0\n1 1 0 1\t\t0\n1 1 1 0\t\t0\n1 1 1 1\t\t0\n')
		test.assert_equals(truth_table(TRUE), 'A B C\t\tTRUE(A,B,C)\n\n0 0 0\t\t1\n0 0 1\t\t1\n0 1 0\t\t1\n0 1 1\t\t1\n1 0 0\t\t1\n1 0 1\t\t1\n1 1 0\t\t1\n1 1 1\t\t1\n')

	@test.it('lambda function')
	def testing_lambda_function():
		test.assert_equals(truth_table(anonymous_function), 'A B C\t\tf(A,B,C)\n\n0 0 0\t\t1\n0 0 1\t\t0\n0 1 0\t\t1\n0 1 1\t\t0\n1 0 0\t\t1\n1 0 1\t\t0\n1 1 0\t\t1\n1 1 1\t\t1\n')


给你一个布尔函数（即一个接受布尔参数并返回布尔值的函数）。你必须返回一个代表该函数真值表的字符串。

格式化规则:
变量应该被命名为A、B、C、D......，以此类推，与传递给布尔函数的顺序相同。
不会有超过26个（A...Z）的参数
布尔值将用1（真）或0（假）表示
如果该函数是匿名的，则使用字母f作为名称。
第一行将包括，按顺序。
变量的名称，用空格（ ）分隔
两个制表符（\t）。
函数名称，括号内的参数用逗号（,）隔开
两个换行符（\n）。
下面几行将依次包括。
变量的值，用空格（ ）分隔
两个制表符（\t）。
这个变量排列的函数结果
一个换行符（\n）。
例子
A B AND(A,B)

0 0 0
0 1 0
1 0 0
1 1 1
值的排序:
请注意数值的排序方式。如果我们把变量的值组合在一起，形成一个二进制数字，那么这个数字在每一行都会递增1。例如，有3个变量:

000
001
010
011
100
101
110
111

通过www.DeepL.com/Translator（免费版）翻译
'''

def truth_table (boolean_function):
    return ""