'''
https://www.codewars.com/kata/5a54e796b3bfa8932c0000ed/train/python


'''

def jumping_number(number):
    number = [int(i) for i in str(number)]
    judge = ([abs(x-y)==1 for x,y in zip((number)[:-1],number[1:])]).count(0) == 0
    return "Jumping!!" if judge else "Not!!"