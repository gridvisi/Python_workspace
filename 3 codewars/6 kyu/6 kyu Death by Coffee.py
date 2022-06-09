'''
https://www.codewars.com/kata/death-by-coffee/train/python

# Show returned limits
def show(y, m, d, result):
    print("{:04}{:02}{:02} returns: {}".format(y, m, d, result))
    return result

test.describe("Example tests")

test.it("exJohn")
y,m,d = 1950, 1, 19
test.assert_equals(show(y,m,d,coffee_limits(y,m,d)), [2645, 1162])
print('<COMPLETEDIN::>')

test.it("exSusan")
y,m,d = 1965,12,11
test.assert_equals(show(y,m,d,coffee_limits(y,m,d)), [111,0])
print('<COMPLETEDIN::>')

test.it("exElizabeth")
y,m,d = 1964, 11, 28
test.assert_equals(show(y,m,d,coffee_limits(y,m,d)), [0, 11])
print('<COMPLETEDIN::>')

test.it("exPeter")
y,m,d = 1965, 9, 4
test.assert_equals(show(y,m,d,coffee_limits(y,m,d)), [0, 0])
print('<COMPLETEDIN::>')
print('<COMPLETEDIN::>')
'''
y,m,d, result = 2006,8,13 ,[100,99]   #,result
def show(y, m, d, result):
    result = ("{:04}{:02}{:02} returns: {}".format(y, m, d, result))
    return result
print(show(y, m, d,result))

def show(y, m, d):
    return "{:04}{:02}{:02}".format(y, m, d)
print(show(y, m, d))