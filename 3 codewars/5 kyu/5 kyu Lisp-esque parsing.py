'''


parse('(sum 2 (mul 5 6))', f) == 32
parse('(sqr (neg 5))', f)     == 25
parse('(pow 2 (sum 2 6))', f) == 256
'''

f = {
    'sum': lambda a, b: a + b,
    'mul': lambda a, b: a * b,
    'div': lambda a, b: a / b,
    'pow': lambda a, b: a ** b,
    'neg': lambda a: -a,
    'sqr': lambda a: a*a
}
a,b = 2,3
print(f['sum'],[2,3])