'''
https://www.codewars.com/kata/525821ce8e7b0d240b002615/train/python

'''

def camelize(str_):
    s = [i for i in str_ if not i.alpha()]
    return ''.join([w.capitalize() for w in str_.lower().split(" ")])
str_ = "cODE=>warS"
print(camelize(str_))