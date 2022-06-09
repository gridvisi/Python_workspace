'''
https://www.codewars.com/kata/5a1a9e5032b8b98477000004/train/python
'''

def even_last(numbers):
    # your code here
    return sum([e for i,e in enumerate(numbers) if i%2==0]) * numbers[-1] if len(numbers)>0 else 0


def even_last(numbers):
    return sum(numbers[::2]) * numbers[-1] if numbers else 0

def even_last(num):
    return num and sum(num[::2]) * num[-1] or 0