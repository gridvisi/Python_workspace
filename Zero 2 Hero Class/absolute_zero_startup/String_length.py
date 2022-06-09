# Python program to find the length of an array

#1
print(12345679 * 7) # *是乘号的意思
print("BBQ") #自助餐

#2
print('丁丁猫') #切换时机

#3
print(1 + 1, 2 - 1, 3 * 3, 3 / 2, 3//2, 3 % 2) #四则

#4
print("The quick brown fox jumps over a lazy dog")

#5
import string
print(string.ascii_lowercase) #小写 printer 打印机
aaa = string.ascii_lowercase
student = "秦子东"
name = "李乐然"
first_name = '李'
last_name = '乐然'
print(student + name)
#6
print('x = ', aaa)
'''
George = ["j","k","l","m","n","o","p","q"]
print(George) 
'''
# nameErro: name "aaa" is not defined

# lowercase 小写  li Li
# 字符串 李老师
# str

import string  #字符串
print(string.ascii_letters)
print(string.digits)
# abcdefghijklmnopqrstuvwxyz
# 常用的python函数


# Ddm2022

'''
len('123')
range(1,10)
'''


#译成中文是：这只伶俐的棕色狐狸跳过一只懒惰的狗。



def find_len(arr):
    # Initialize the counter with 0
    count = 0

    # Run a for loop to go through all the elements of the array
    for element in arr:
        # For each element in array increase the counter by 1
        count = count + 1

    # Return the value of counter after exiting the for loop
    return count


# Function Call:
arr = [1, 2, 3, 4, 5]
answer = find_len(arr)
print(f"The length of array {arr} is {answer}.")

######################  Output  ######################
# The length of array [1, 2, 3, 4, 5] is 5.