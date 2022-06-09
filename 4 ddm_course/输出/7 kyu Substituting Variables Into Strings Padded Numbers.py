'''
https://www.codewars.com/kata/51c89385ee245d7ddf000001/solutions/python
'''

def solution(value):
    return "Value is %05d" % value

def solution(value):
    return f'Value is {value:05d}'

solution= "Value is {:05}".format

solution='Value is {:05d}'.format


def solution(value):
    num = 5 - len(str(value))
    zeros = ""
    for i in range(num):
        zeros += "0"
    return("Value is {}".format(zeros + str(value)))

