# https://www.codewars.com/kata/586430a5b3a675296a000395/train/python

'''
import codewars_test as test
from solution import insurance

@test.describe('Example Tests')
def example_tests():
    @test.it('Example Test Case')
    def example_test_case:
        test.assert_equals(insurance(18, "medium", 7), 490)
        test.assert_equals(insurance(30,"full-size",30),1950)
        test.assert_equals(insurance(21,"economy",-10), 0)
        test.assert_equals(insurance(42,"my custom car",7), 455)

'''

def allow_plate(day):
    num_plate = ['渝A9919', '渝C5072', '渝A7R69', '渝A2966',
             '渝D8371', '渝A3417', '渝A5255', '渝AD991']

    week = ['Mon','Tue','Wed','Thu','Fri']
    num = list(range(10))
    rule = {}
    i = 0
    for d in week:
        rule[d] = num[i::5]
        i += 1
    return rule[day]
day = 'Fri'
print(allow_plate(day))


# Odd_even allow
num_plate = ['渝A9919', '渝C5072', '渝A7R69', '渝A2966',
             '渝D8371', '渝A3417', '渝A5255', '渝AD991']

for plate in num_plate:
    if eval(plate[-1]) % 2 == 1:
        #单号上路的车牌
        print(plate)

a = 0
while a < len(num_plate) :
    b = num_plate[a]
    c = b[5]
    if c == '5' or c == '0':
        print(b)
    a += 1