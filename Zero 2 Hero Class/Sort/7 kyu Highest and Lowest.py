#https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python
'''

high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
'''

def high_and_low(numbers):
    # ...
    n = sorted(numbers.split(' '),key=lambda x:eval(x))
    #n = sorted(numbers.split(' '))
    return ' '.join([n[-1],n[0]])
numbers = "4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"  # "542 -214"
print(high_and_low(numbers))

#1st
def high_and_low(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))

#2nd
def high_and_low(numbers):
  n = map(int, numbers.split(' '))
  return str(max(n)) + ' ' + str(min(n))

#3rd
def high_and_low(numbers):
    n = map(int, numbers.split(' '))
    return "{} {}".format(max(n), min(n))

#4th
def high_and_low(numbers):
    nums = sorted(numbers.split(), key=int)
    return '{} {}'.format(nums[-1], nums[0])

#5th
def high_and_low(numbers):
  return " ".join(x(numbers.split(), key=int) for x in (max, min))

#6th
def high_and_low(numbers):
    nums = [int(x) for x in numbers.split(" ")]
    return f'{max(nums)} {min(nums)}'

