'''
https://www.codewars.com/kata/5cfe4465ac68b86026b09c77/train/python

考虑以下众所周知的规则。

如果一个数字的位数之和可以被3整除，那么这个数字就可以被3整除 我们把3叫做 "1和 "质数。
对于37，我们从右边取3组数字，检查这些组的和是否被37整除。例子 37 * 123456787 = 4567901119 => 4 + 567 + 901 + 119 = 1591 = 37 * 43. 因为我们使用的是3的组数，所以我们称之为 "3和 "质数。
对于41，我们从右边取5组数字，检查这些组的和是否被41所除。这就是一个 "5和 "质数。
其他的例子。239是 "7和 "质数(7组), 而199是 "99和 "质数(99组).
让我们看看另一种类型的质数。

对于11，我们需要把所有的数字加起来 通过交替他们的符号从右边开始。例子：11 * 123456 = 1358016 => 6-1+0-8+5-3+1 = 0，它可以被11所除。我们把这个叫做 "1-altsum "质数。
对于7，我们需要从右边开始将数字分成3组，并将所有组数交替符号相加。例如：7 * 1234567891234 = 8641975238638 => 638 - 238 + 975 - 641 + 8 = 742/7 = 106。
7是一个 "3-altsum "质数，因为我们使用的是3组。47 是 "23-altsum"（23 的组），而 73 是 "4-altsum "质数（4 的组）。
你会得到一个质数p，你的任务是找到最小的正整数n，使p的可分性测试为n和或n-altsum。

例如，你的任务是

解(3)="1 -sum"
solve(7)="3-altsum"
首字母不会超过50,000,000。更多的例子在测试案例中。

Test.it("Basic tests")
Test.assert_equals(solve(3),"1-sum")
Test.assert_equals(solve(7),"3-altsum")
Test.assert_equals(solve(11),"1-altsum")
Test.assert_equals(solve(13),"3-altsum")
Test.assert_equals(solve(37),"3-sum")
Test.assert_equals(solve(47),"23-altsum")
Test.assert_equals(solve(73),"4-altsum")
Test.assert_equals(solve(239),"7-sum")
Test.assert_equals(solve(376049),"47006-altsum")
Test.assert_equals(solve(999883),"499941-sum")
Test.assert_equals(solve(24701723),"12350861-sum")
Test.assert_equals(solve(45939401),"11484850-altsum")
'''

def solve(p):
    pass