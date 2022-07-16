'''
https://www.codewars.com/kata/5672a98bdbdd995fad00000f/train/python
'''
def rps(p1, p2):
    #your code here
    rules = {
            'rock':'scissors',
            'paper':'rock',
            'scissors':'paper'
            }
    if rules[p1] == p2:
        return 'Player 1 won!'
    elif rules[p2] == p1: #key:p2,p1:value
        return 'Player 2 won!'
    return 'Draw!'

#dict

#collections
#assignment

wangs_name = '王雨桐'
wangs_Ename = 'alexwang'
class_list = ['mcree','lzj','bill gates']
class_list.append(wangs_Ename)
print(class_list)

class_dict = {'alexwang':'王雨桐'}
print(class_dict['alexwang'])
emergence_call = {'110':'police','114':'inquiry'}


num = [1,2,3,4,5]
num[0] = 6
print(num)
numtuple = (1,2,3,4,5)
#numtuple[0] = 6
print(num)

sheepDot = {1:[20,30,80,90,20,30],
            2:[40,80,20,60,50]}

print(sheepDot[1][::-1]) #歧义


age = [17,13,15]
print('index',age.index(15))
#1
print(age[0] > age[1])
#2 如果 True：
#swap
age[0] , age[1] = age[1] , age[0]
print(age)
#age = [13,15,17]
