'''
https://www.codewars.com/kata/shortest-steps-to-a-number/train/python
Given a number, num, return the shortest amount of steps it would take from 1, to land exactly on that number.

Description:
A step is defined as:

Adding 1 to the number: num += 1
Doubling the number: num *= 2
You will always start from the number 1 and you will have to return the shortest count of steps it would take to land exactly on that number.
1 <= num <= 10000
Examples:
'''
num = 12
def shortest_steps_to_num(num):
    re = []
    quot,rem = num//2,num%2
    if quot == 2 ** (len(quot)-2):
        if e == '1':
            re.append(i)
    return step,re
print(shortest_steps_to_num(num))


'''
def shortest_steps_to_num(num):
    re = []
    step = str(bin(num))[::-1][:-2]
    for i,e in enumerate(step):
        if e == '1':
            re.append(i)
    return step,re
print(shortest_steps_to_num(num))
'''