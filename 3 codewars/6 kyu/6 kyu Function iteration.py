'''
https://www.codewars.com/kata/function-iteration/train/python
Test.describe("Iterator for 'get_double' function")
def get_double(n):
    return 2*n

Test.it("Running the iterator for once")
double_iterator = create_iterator(get_double, 1)

Test.assert_equals(double_iterator(3), 6)
Test.assert_equals(double_iterator(5), 10)

Test.it("Running the iterator twice")
get_quadruple = create_iterator(get_double, 2)

Test.assert_equals(get_quadruple(2), 8)
Test.assert_equals(get_quadruple(5), 20)
'''
def get_double(n):
    return 2*n

def create_iterator(func, n):

    i = (i for i in range(n))
    it = iter(i)
    res = func

    return res
n = 2
func = get_double(n)
print(create_iterator(func, 3))

def create_iterator(func, n):
    def f(x):
        for i in range(n):
            x = func(x)
        return x
    return f

def create_iterator(func, n):
  if n == 1: return func
  return lambda x : func(create_iterator(func, n-1)(x))
print(create_iterator(func, 3))