'''
https://www.codewars.com/kata/51c89385ee245d7ddf000001/train/python
'''


def solution(value):
    s = [0]*5
    print(str(value)[1])
    return ''.join([str(value)[i] if i < len(str(value)) else 0 for i in range(5)])

def solution(value):

    return f"Value is {(5 - len(str(value)))*'0'}{value}"
value = 1024
print(solution(value))