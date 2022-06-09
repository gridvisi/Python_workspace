'''
https://www.codewars.com/kata/shortest-steps-to-a-number/train/python
Adding 1 to the number: num += 1
Doubling the number: num *= 2
You will always start from the number 1 and you will have to return the shortest count of steps it would take to land exactly on that number.
1 <= num <= 10000
Test.assert_equals(shortest_steps_to_num(1), 0);
Test.assert_equals(shortest_steps_to_num(12), 4);
Test.assert_equals(shortest_steps_to_num(16), 4);
Test.assert_equals(shortest_steps_to_num(71), 9);
'''
ct = 0
#print(12//2,6//2)
def shortest_steps_to_num(num,ct=0):
    if num == 1:
        return ct
    elif num%2 == 1:
        #re = num//2
        ct += 2
        return shortest_steps_to_num(num//2,ct)
    elif num%2 == 0:
        ct += 1
        return shortest_steps_to_num(num // 2,ct)

print(shortest_steps_to_num(16,0))

def shortest_steps_to_num(num):
    return num.bit_length() + bin(num).count('1') - 2

def shortest_steps_to_num(num):
    steps,re = 0,[]
    while num != 1:
        if num % 2:
            #re.append([num // 2, num % 2])
            num -= 1

        else:
            re.append([num // 2, num % 2])
            num //= 2
        re.append([num // 2,num % 2])
        steps += 1
    return steps,re


num = 71
print(shortest_steps_to_num(num))
print(num.bit_length(),bin(num).count('1'))

'''
step = 0
def shortest_steps_to_num(num):
    quot,rem = num//2,num%2
    global step

    if rem == 0 and quot >= 1:
        step += 1
        
        return shortest_steps_to_num(quot)

    elif rem == 1 and quot >= 1:
        step += 2
        
        return shortest_steps_to_num(quot)
    return step
'''