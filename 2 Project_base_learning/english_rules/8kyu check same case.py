'''
https://www.codewars.com/kata/5dd462a573ee6d0014ce715b/train/python

Write a function that will check if two given characters are the same case.

If any of characters is not a letter, return -1
If both characters are the same case, return 1
If both characters are letters and not the same case, return 0
Examples
'a' and 'g' returns 1

'A' and 'C' returns 1

'b' and 'G' returns 0

'B' and 'g' returns 0

'0' and '?' returns -1
'''

import string
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)
print(string.Template)


#Step 1st




def same_case(a, b):
    if a in string.punctuation or b in string.punctuation:
        return -1

    elif a.islower() and b.islower():
        return 1

    elif a.isupper() and b.isupper():
        return 1

    elif a.islower() != b.islower():
        return 0

print("\t:",'\t'.isalpha())

a,b = '\t', 'Z'
print(f"{a} {b}:",(a+b).isalnum())

a,b = '-1', '5'
print(f"{a} {b}:",(a+b).isalnum())

a,b = 'H', ':'
print(f"{a} {b}:",(a+b).isalnum())

a,b = 'Html', '5'
print(f"{a} {b}:",(a+b).isalnum())

print("-1:",'-1'.isalnum()) #负数字符串false
print("*t:",'*t:'.isalnum())
print("3t:",'3t'.isalnum())

print("\t:",'3'.isalpha())
print("\t:",'a'.isalpha())
print("\t:",':'.isalpha())


#step 2nd
import string
def same_case(a, b):
    if a in string.punctuation or b in string.punctuation:
        return -1

    elif a.islower() and b.islower():
        return 1

    elif a.isupper() and b.isupper():
        return 1

    elif a.islower() != b.islower():
        return 0

    else:
        return -1


'''
random test 有 4 栗子报错！全是 0 should equal -1
'''

# step 3rd
import string

def same_case(a, b):
    if [1 for c in a+b if c in string.punctuation]:
        return -1

    elif a.islower() and b.islower():
        return 1

    elif a.isupper() and b.isupper():
        return 1

    elif a.islower() != b.islower():
        return 0

    else:
        return -1

# 6个栗子报错 都是 0 should equal -1
# 第一个if判断网眼大了，有些用例漏过了



# step 4th
def same_case(a, b):
    if (a+b).isalnum() == False:
        print('a+b:',(a+b).isalnum())
        return -1

    if a.islower() == b.islower():
        return 1

    if a.islower() != b.islower():
        return 0

a, b = 'H', ':'
print(bool(a.isalnum() and b.isalnum()))
print(not (a.isalpha and b.isalpha))

a, b = '-1', "0"
print(same_case(a, b))


#5th
def same_case(a, b):
    if a.isalnum() and b.isalnum():
        if a.islower() != b.islower():
            return 0
        else:
            return 1
    else:
        return -1

a, b = 'H', ':'
print('-1 is lower?','1'.islower())
print(bool(a.isalnum() and b.isalnum()))
print(not (a.isalpha and b.isalpha))

a, b = '@B1', "aG"
print(same_case(a, b))