'''
https://www.codewars.com/kata/586bca7fa44cfc833e00005c/train/python


'''

def create_array_of_tiers(n):
    # your awesome code here
    return [str(n)[:i] for i,e in enumerate(str(n),1)]
n = 420
print(create_array_of_tiers(n))