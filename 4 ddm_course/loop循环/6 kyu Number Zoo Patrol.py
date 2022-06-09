'''
https://www.codewars.com/kata/5276c18121e20900c0000235/train/python
'''

def find_missing_number(numbers):
    for i in range(1,max(numbers),1):
        if i not in numbers:
            return i
numbers = [4, 2, 3]
print(find_missing_number(numbers))