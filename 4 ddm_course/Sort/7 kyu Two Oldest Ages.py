'''
https://www.codewars.com/kata/511f11d355fe575d2c000001/train/python
'''
ages = [6, 5, 83, 5, 3, 18]
print(sorted(ages))
def two_oldest_ages(ages):
    return sorted(ages)[-2:]
print(two_oldest_ages(ages))