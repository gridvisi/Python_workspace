'''
https://www.codewars.com/kata/5e96332d18ac870032eb735f/train/python

'''

def womens_age(n):
    # your code here
    return f"{n}? That's just {21 if n%2 else 20}, in base {(n-1)//2 if n%2 else n//2}!"

n = 32
print(womens_age(n))

#1
def womens_age(n):
    return f"{n}? That's just {20+n%2}, in base {n//2}!"