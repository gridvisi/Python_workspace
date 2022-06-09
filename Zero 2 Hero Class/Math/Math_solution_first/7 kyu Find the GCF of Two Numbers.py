'''
https://www.codewars.com/kata/579e3476cf1fa55592000045/train/python

Your task here is the find the GCF (Greatest Common Factor) of any two numbers passed into a method, which will return one integer answer as an output.

Examples:

find_GCF(4, 6) # Should return 2
find_GCF(93, 186) # Should return 93
find_GCF(20, 5) # Should return 5
Here, inputs will always be natural numbers so there's no need to worry about negative
values or zero.

test.assert_equals(find_GCF(2, 4), 2)
test.assert_equals(find_GCF(8,20), 4);
test.assert_equals(find_GCF(5,13), 1);
test.assert_equals(find_GCF(100,100), 100);

ALGORITHMSNUMBERSMATHEMATICS
'''

def find_GCF(a, b):
    a,b = max(a,b),min(a,b)
    a,b = sorted([a,b])
    while b%a != 0:
        a,b = b%a,a
    return a
a,b = 12,18
print(find_GCF(a,b))

#1st
def find_GCF(a, b):
    if b == 0: return a
    return find_GCF(b,a%b)