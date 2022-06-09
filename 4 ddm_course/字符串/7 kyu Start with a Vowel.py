'''
https://www.codewars.com/kata/5a02e9c19f8e2dbd50000167/train/python

import codewars_test as test
from solution import vowel_start

@test.describe('Fixed Tests')
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_tests():
        test.assert_equals(vowel_start('It is beautiful weather today!'), 'it isb e a ut if ulw e ath ert od ay',)
        test.assert_equals(vowel_start('Coding is great'),'c od ing isgr e at',)
        test.assert_equals(vowel_start('my number is 0208-533-2325'),'myn umb er is02085332325' ,)
        test.assert_equals(vowel_start('oranges, apples, melon, pineapple'), 'or ang es appl esm el onp in e appl e', )
        test.assert_equals(vowel_start('under_score'), 'und ersc or e')
'''
st = 'my number is 0208-533-2325'
def vowel_start(st):
    ans = ''
    i,j = 0, 1
    vow = ['a','e','i','o','u']
    while i < j < len(st):
        if st[i] in vow and st[j] not in vow:
            ans += st[i:j+1]
        else:
            
    # your code here
    pass