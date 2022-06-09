# def square_sum(numbers):
#  https://www.codewars.com/kata/square-n-sum/python
numbers = [1, 2, 2]
def square_sum(numbers):
    return sum(map(lambda x:x**2,[i for i in numbers]))

def square_sum(numbers):
    return sum(x ** 2 for x in numbers)
def square_sum(numbers):
    return sum(map(lambda x: x**2,numbers))

def square_sum(numbers):
    return sum([x**2 for x in numbers])
print(square_sum(numbers))