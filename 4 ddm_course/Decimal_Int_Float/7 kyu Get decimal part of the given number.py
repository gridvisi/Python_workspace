'''

https://www.codewars.com/kata/586e4c61aa0428f04e000069/train/python
'''

def get_decimal(n):
    return abs(n) % 1

def get_decimal(n):
    n = abs(n)
    return n - int(n)


def get_decimal(n): return abs(n - int(str(n).split('.')[0]))


#fail try
def get_decimal(n):
    # your code here
    return float('.'+str(n).split(".")[-1])
n = 1.9
print(get_decimal(n))


#延申任务：整型和小数部分分别存放

def get_decimal_float(n):
    return int(n),abs(n)%1  #n - abs(n)%1



n = 3.14
print(get_decimal_float(n))
