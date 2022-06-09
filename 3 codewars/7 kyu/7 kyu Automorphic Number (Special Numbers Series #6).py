'''
Definition
A number is called Automorphic number if and only if its square ends in the same digits as the number itself.

Task
Given a number determine if it Automorphic or not .
'''

def automorphic(n):
    x = n
    if str(n*n)[-len(str(n)):] == str(n):return "Automorphic"
    else:return "Not!!"

def automorphic(n):
    return "Automorphic" if str(n*n).endswith(str(n)) else "Not!!"

def automorphic(n):
    return "Automorphic" if str(n**2).endswith(str(n)) else "Not!!"

def automorphic(n):
    return "Automorphic" if n == (n ** 2) % 10 ** len(str(n)) else "Not!!"

n = 325
print(str(n*n)[-len(str(n)):])
print(automorphic(n))

