'''
https://www.codewars.com/kata/56f173a35b91399a05000cb7/train/python

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(find_longest("The quick white fox jumped around the massive dog"), 7)
        test.assert_equals(find_longest("Take me to tinseltown with you"), 10)
        test.assert_equals(find_longest("Sausage chops"), 7)
        test.assert_equals(find_longest("Wind your body and wiggle your belly"), 6)
        test.assert_equals(find_longest("Lets all go on holiday"), 7)
'''

def find_longest(string):
    spl = string.split(" ")
    print(spl)
    longest = 0
    i=0
    while i < len(spl):
        if len(spl[i]) > longest:
            longest = len(spl[i])
        i += 1
            #print(spl[i],longest)
    return longest
string = "The quick white fox jumped around the massive dog"
print(find_longest(string))


#1st
def find_longest(strng):
    return max(len(a) for a in strng.split())