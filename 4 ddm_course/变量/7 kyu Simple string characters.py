'''
https://www.codewars.com/kata/5a29a0898f27f2d9c9000058/train/python

Test.it("Basic tests")
Test.assert_equals(solve("Codewars@codewars123.com"),[1,18,3,2])
Test.assert_equals(solve("bgA5<1d-tOwUZTS8yQ"),[7,6,3,2])
Test.assert_equals(solve("P*K4%>mQUDaG$h=cx2?.Czt7!Zn16p@5H"),[9,9,6,9])
Test.assert_equals(solve("RYT'>s&gO-.CM9AKeH?,5317tWGpS<*x2ukXZD"),[15,8,6,9])
Test.assert_equals(solve("$Cnl)Sr<7bBW-&qLHI!mY41ODe"), [10,7,3,6])
Test.assert_equals(solve("@mw>0=QD-iAx!rp9TaG?o&M%l$34L.nbft"), [7,13,4,10])

Solve("*'&ABCDabcde12345") = [4,5,5,3].
--the order is: uppercase letters, lowercase, numbers and special characters.
'''

def solve(s):
    upper,low,num,char = 0,0,0,0
    for c in s:
        if c.isupper():
            upper += 1
        elif c.islower():
            low += 1
        elif c.isdigit():
            num += 1
        else:# c.isalpha():
            char += 1
    return [upper,low,num,char]
s = "*'&ABCDabcde12345"
print(solve(s))