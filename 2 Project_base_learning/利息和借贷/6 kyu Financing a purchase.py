'''
https://www.codewars.com/kata/59c68ea2aeb2843e18000109/train/python

说明比较长，但它试图解释什么是融资计划。

固定利率抵押贷款的固定月供是指借款人每月支付的金额，以确保贷款期满后连本带利全部还清。

月供的计算公式是根据年金公式计算的。月供c取决于。

利率 -- 月利率用小数点表示，而不是百分比。月利率只是将给定的年利率百分比除以100，再除以12。

期限--每月还款的次数，称为贷款期限。

本金--借款金额，称为贷款本金（或余额）。

首先我们要确定c。

我们有：c = n /d，其中n = r *余额，d = 1 - (1 + r)**(-term)，其中**是幂函数（可以看下面的参考资料）。

支付c由两部分组成。第一部分支付给定月份余额的利息（我们称它为int），第二部分偿还余额（我们称这部分为princ），因此对于下个月，
我们得到新的余额=旧的余额-princ，c=int+princ。

贷款的结构是这样的，即归还借款人的本金数额一开始是很小的，随着每次按揭付款而增加。前几年的按揭付款主要是支付利息，而最后几年的
付款主要是偿还本金。

按揭贷款的分期付款表可以详细了解每笔按揭付款中专门用于每一部分的具体比例。

以一个10万美元、30年、利率为6厘的抵押贷款为例，其摊还计划表由360个月付款组成。下面的部分摊还时间表用2个小数浮动显示了本金和利
息支付之间的余额。

--	num_payment	c	princ	int	Balance
--	1	599.55	99.55	500.00	99900.45
--	...	599.55	...	...	...
--	12	599.55	105.16	494.39	98,771.99
--	...	599.55	...	...	...
--	360	599.55	596.57	2.98	0.00

Task:
Given parameters

rate: annual rate as percent (don't forgent to divide by 100*12)
bal: original balance (borrowed amount)
term: number of monthly payments
num_payment: rank of considered month (from 1 to term)
the function amort will return a formatted string:

"num_payment %d c %.0f princ %.0f int %.0f balance %.0f" (with arguments num_payment, c, princ, int, balance)

In Common Lisp: return a list with num-payment, c, princ, int, balance each rounded.

Examples:
amort(6, 100000, 360, 1) ->
"num_payment 1 c 600 princ 100 int 500 balance 99900"

amort(6, 100000, 360, 12) ->
"num_payment 12 c 600 princ 105 int 494 balance 98772"
Ref
https://en.wikipedia.org/wiki/Mortgage_calculator

FUNDAMENTALSMATHEMATICSALGORITHMSNUMBERS

test.assert_equals(amort(7.4, 10215, 24, 20), "num_payment 20 c 459 princ 445 int 14 balance 1809")
test.assert_equals(amort(7.9, 107090, 48, 41), "num_payment 41 c 2609 princ 2476 int 133 balance 17794")
test.assert_equals(amort(6.8, 105097, 36, 4), "num_payment 4 c 3235 princ 2685 int 550 balance 94447")
test.assert_equals(amort(3.8, 48603, 24, 10), "num_payment 10 c 2106 princ 2009 int 98 balance 28799")
test.assert_equals(amort(1.9, 182840, 48, 18), "num_payment 18 c 3959 princ 3769 int 189 balance 115897")
test.assert_equals(amort(1.9, 19121, 48, 2), "num_payment 2 c 414 princ 384 int 30 balance 18353")
test.assert_equals(amort(2.2, 112630, 60, 11), "num_payment 11 c 1984 princ 1810 int 174 balance 92897")
test.assert_equals(amort(5.6, 133555, 60, 53), "num_payment 53 c 2557 princ 2464 int 93 balance 17571")
test.assert_equals(amort(9.8, 67932, 60, 34), "num_payment 34 c 1437 princ 1153 int 283 balance 33532")
test.assert_equals(amort(3.7, 64760, 36, 24), "num_payment 24 c 1903 princ 1829 int 75 balance 22389")
'''

