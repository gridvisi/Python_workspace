'''
https://www.codewars.com/kata/5a53a17bfd56cb9c14000003/train/python
Input >> Output Examples
disariumNumber(89) ==> return "Disarium !!"
Explanation:
Since , 81 + 92 = 89 , thus output is "Disarium !!"
'''


def disarium_number(number):
    disarium = [int(e)**(i+1) for i,e in enumerate(str(number))]
    print(disarium)
    return "Disarium !!" if sum(disarium) == number else "Not !!"
number = 89
print(disarium_number(number))