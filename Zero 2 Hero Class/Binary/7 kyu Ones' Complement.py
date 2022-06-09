'''
https://www.codewars.com/kata/59b11f57f322e5da45000254/train/python

Test.assert_equals(ones_complement("0"), "1")
Test.assert_equals(ones_complement("1"), "0")
Test.assert_equals(ones_complement("01"), "10")
Test.assert_equals(ones_complement("10"), "01")
Test.assert_equals(ones_complement("1101"), "0010")
'''

#10th solve by ericlee
def ones_complement(binary_number):
    return ''.join([str(0+ (eval(i)!=1)) for i in binary_number])
binary_number = '1101'
print(ones_complement(binary_number))


#1st

def ones_complement(n):
    return n.translate(str.maketrans("01","10"))

def ones_complement(binary_number):
  return ''.join('0' if int(n) else '1' for n in binary_number)