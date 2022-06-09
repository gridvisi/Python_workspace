'''
https://www.codewars.com/kata/5ac54bcbb925d9b437000001/train/python

Test.assert_equals(find_middle('s7d8jd9'), 0)
Test.assert_equals(find_middle('58jd9fgh/fgh6s.,sdf'), 16)
Test.assert_equals(find_middle(None), -1)
Test.assert_equals(find_middle([1,2,3]), -1)
'''
import string
def find_middle(strng):
    if not string:return -1
    if all([not(i.isdigit()) for i in strng]):return -1
    if all([isinstance(i,int) for i in strng]):return -1
    if not strng.isalnum():return -1
    n = eval('*'.join([i for i in strng if i.isdigit()]))
    return str(n)[len(str(n))//2-1:len(str(n))//2+1] if len(str(n))%2== 0 else str(n)[len(str(n))//2]
strng = '58jd9fgh/fgh6s.,sdf'
strng = 's7d8jd9'
strng = [1,2,3]
strng = 'asd.fasd.gasdfgsdfgh-sdfghsdfg/asdfga=sdfg'
strng = ['a', 'b', 'c']
print(find_middle(strng))