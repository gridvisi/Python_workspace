'''
https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python
test.assert_equals(descending_order(0), 0)
test.assert_equals(descending_order(15), 51)
test.assert_equals(descending_order(123456789), 987654321)
'''

def descending_order(num):
    return int(''.join(sorted(str(num),reverse=True)))
num = 123456789
#num = '123456789'
print(descending_order(num))

num = ['9', '8', '7', '6', '5', '4', '3', '2', '1']
print(max(num),min(num))