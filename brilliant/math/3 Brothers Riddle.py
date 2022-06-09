'''
3 Brothers Riddle
三兄弟之谜
Number Theory Level 5
数论5级
Once upon a time, there were 33 brothers living in a small remote village,
with no extra-ordinary features. Nonetheless, the old wiseman of the village
once told all 33 brothers that their age combination was so unique that no younger
men on Earth could resemble: when the product of any 22 brothers' ages was divided by the other one's age, the remainder would always be 66. Also, the eldest age is less than twice the youngest age.
从前，有3个兄弟住在一个偏僻的小村子里，没有什么特别的地方。尽管如此，村里的老智者曾经告诉所有3个兄弟，
他们的年龄组合是如此独特，地球上没有年轻人能像这样：当任何2个兄弟年龄的乘积除以另一个兄弟的年龄时，
剩下的永远是6岁。而且，最大的年龄不到最小年龄的两倍。
What would be the sum of all 33 brothers' ages?
3个兄弟的年龄总和是多少？
'''
age = [i for i in range(1,150)]

for b in age:
    for m in age:
        for s in age:
            if (b*m)%s == 6 and (b*s)%m == 6 and (m*s)%b == 6:
                if b < 2*s and b > m > s:
                    print(b,m,s)