'''
https://www.codewars.com/kata/525f039017c7cd0e1a000a26/train/python

  87 +   78 =  165     - step 1, not a palindrome
 165 +  561 =  726     - step 2, not a palindrome
 726 +  627 = 1353     - step 3, not a palindrome
1353 + 3531 = 4884     - step 4, palindrome!
'''

m = '07'
print(int(m))

def palindrome_chain_length(n):
    x = n
    step = 0
    while str(x) != str(x)[::-1]:
        x += int(str(x)[::-1])
        step += 1
    return step
n = 87
#n = 10
print(palindrome_chain_length(n))

#Execution Timed Out
#Execution Timed Out (12000 ms)
def palindrome_chain_length(n):
    x = n
    step = 0
    while str(x) != str(x)[::-1]:
        while x%10 ==0:
            x = x//10
        x += eval(str(x)[::-1])
        step += 1
    return step

#1st
def palindrome_chain_length(n):
    steps = 0
    while str(n) != str(n)[::-1]:
        n = n + int(str(n)[::-1])
        steps += 1
    return steps