'''
https://brilliant.org/daily-problems/plussed/


'''

import fractions
r = 1/9
s = 1
s_centre = r * s
s_branch = r * s * r * 2

def square(step):
    r = 1 / 9
    s_centre = r * 1
    riter = r*r
    s_branch = riter * 2
    cunt = 1
    while cunt < step:
        riter *= r
        s_branch += riter * 2 * 3**cunt
        cunt += 1
    return 4*s_branch + s_centre
print(square(100))
print(2/9,7/27,8/27,1/3)

#fractions.Fraction(round(s_branch + s_centre),2),

import fractions
for num, decimal in [(3, 2), (2, 5), (30, 4)]:
    fract = fractions.Fraction(num, decimal)
    print('{}/{} = {}'.format(num, decimal, fract))

for deci in ['0.6', '2.5', '2.3', '4e-1']:
    fract = fractions.Fraction(deci)
    print('{0:>4} = {1}'.format(deci, fract))
