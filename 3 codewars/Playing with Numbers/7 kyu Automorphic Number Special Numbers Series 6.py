'''
https://www.codewars.com/kata/5a58d889880385c2f40000aa/train/python
Definition
A number is called Automorphic number if and only if its square ends in the same digits as the number itself.


定义
当且仅当一个数的平方结尾与该数本身的数字相同时，该数被称为自动数。
'''

def automorphic(n):
    return "Automorphic" if str(int(str(n)[-1])**2)[-1] == str(n)[-1] else "Not!!"