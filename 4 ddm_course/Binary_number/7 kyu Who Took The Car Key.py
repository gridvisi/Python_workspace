'''
https://www.codewars.com/kata/57a23c2acf1fa514d0001034/train/python

Test.describe('Basic Tests')
Test.assert_equals(who_took_the_car_key(
    ['01000001', '01101100', '01100101', '01111000', '01100001', '01101110',
     '01100100', '01100101', '01110010']
), 'Alexander')
Test.assert_equals(who_took_the_car_key(
    ['01001010', '01100101', '01110010', '01100101', '01101101', '01111001']
), 'Jeremy')
Test.assert_equals(who_took_the_car_key(
    ['01000011', '01101000', '01110010', '01101001', '01110011']
), 'Chris')
Test.assert_equals(who_took_the_car_key(
    ['01001010', '01100101', '01110011', '01110011', '01101001', '01100011',
     '01100001']
), 'Jessica')
Test.assert_equals(who_took_the_car_key(
    ['01001010', '01100101', '01110010', '01100101', '01101101', '01111001']
), 'Jeremy')
'''

print(int('0b'+'01000011',2))

def who_took_the_car_key(message):
    return ''.join([chr(int('0b'+ n,2)) for n in message])

message = ['01000011', '01101000', '01110010', '01101001', '01110011']
print(who_took_the_car_key(message))