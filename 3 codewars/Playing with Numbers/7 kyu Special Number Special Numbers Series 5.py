'''
https://www.codewars.com/kata/5a55f04be6be383a50000187/train/python


'''

def special_number(number):
    return "Special!!" if max([int(i) for i in str(number)]) <= 5 else "NOT!!"


def special_number(n):
    return "Special!!" if max(str(n)) <= "5" else "NOT!!"