# https://www.codewars.com/kata/51c89385ee245d7ddf000001/train/python

'''


'''
a = 1
print(str(a) + 'b',1 + 1)
# '1'

print(len(str(a) + 'b'))

# 如果超过10位，那么后面紧跟rmb
def solution(value):
    value = str(value)
    if len(value) <= 5:
       x = 5 - len(value)
       return x*'0' + value

    elif len(value) == 11:
        return value + 'phone.NO'

    elif len(value) >= 10:
        return value + 'rmb'

    else:
        return 'exceed the limit of 5 digit'

value = 12345678910
print(solution(value))