'''
https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python
'''
def high_and_low(numbers):
    # ...
    return max(numbers.split(' '),key=int),min(numbers.split(' '),key=int)
#' '.join([max(numbers.split(' '),key=int),min(numbers.split(' '),key=int)])
numbers = "4 5 29 54 4 0 -214 542 -64 1 -3 6 -6" #542 -214
print(numbers.split(' '),sorted(numbers.split(' ')))
print(high_and_low(numbers))


#1st
def high_and_low(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))

def high_and_low(numbers):
  n = map(int, numbers.split(' '))
  return str(max(n)) + ' ' + str(min(n))

def high_and_low(numbers):
    n = map(int, numbers.split(' '))
    return "{} {}".format(max(n), min(n))