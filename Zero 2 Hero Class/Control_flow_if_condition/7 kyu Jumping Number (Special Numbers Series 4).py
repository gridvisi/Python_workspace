'''
https://www.codewars.com/kata/5a54e796b3bfa8932c0000ed/train/python


'''
#30th code by ericlee
def jumping_number(number):
    number = [int(i) for i in str(number)]
    judge = ([abs(x-y)==1 for x,y in zip((number)[:-1],number[1:])]).count(0) == 0
    return "Jumping!!" if judge else "Not!!"
number = 323
print(jumping_number(number))

#1st
def jumping_number(number):
    arr = list(map(int, str(number)))
    return ('Not!!', 'Jumping!!')[all(map(lambda a, b: abs(a - b) == 1, arr, arr[1:]))]