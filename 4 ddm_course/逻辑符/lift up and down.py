import math
import random

print(5 > 3, 3 > 5)
dice_1 = random.choice([1,2,3,4,5,6])
dice_2 = random.choice([1,2,3,4,5,6])
#dice_3 = random.choice([1,2,3,4,5,6])

print(dice_1 >= dice_2,dice_1,dice_2)

#print('dice:',random.choice([1,2,3,4,5,6]))











'''

r = 3
c = 2 * math.pi*r
print(c)

x,y = 10,8
print(math.gcd(x,y))



def abs(n):
    if n >= 0:
        return n
    return -n

# lift
ground,left,right,call=1,6,2,4
def elevator(ground,left,right,call):
    if abs(call-left) > abs(call-right):
        right = call
        return 'step right'
    elif abs(call-left) < abs(call-right):
        left = call
        return 'step left'
    elif abs(call-left) == abs(call-right):
        return 'step ' + random.choice(['left','right'])

print(elevator(ground,left,right,call))

def elevator(www,left,right,call):
    return "left" if abs(call-left) < abs(call-right)<abs(call-www) else"right"
print(elevator(ground,left,right,call))


left,middle,right,call=3,3,5
def elevator(left,middle,right,call):
  if abs(call-left)>=abs(call-right)>=abs(call-middle):
     return 'right'
  else:
     return 'left'

def elevator(left,middle,right,call):
    return "left" if abs(call-left) < abs(call-right) else"right"

right,middle,left,call=1,2,3,4

def elevator(left,middle,right,call):
    compare = [abs(call-left),abs(call-middle),abs(call-right)]
    return compare



compare = []
right,middle,left,peppo,call=1,2,3,4,5

def elevator(left,middle,right,peppo,call):
    compare = [abs(call-left),abs(call-middle),abs(call-right),abs(call-peppo)]
    return compare


print({right:1, middle:2, left32, peppo:4})
print({right:1, middle:2, left32, peppo:4})

rmb = 1001
wrappers =0
eaten =0

while rmb >0:
    rmb -=1
    eaten +=1
    wrappers +=1

    if wrappers ==3:
        wrappers -=3
        eaten +=1
        wrappers +=1
print("Answer:", eaten)#  Answer: 88573
'''