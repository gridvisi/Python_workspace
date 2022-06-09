#https://stackoverflow.com/questions/419163/what-does-if-name-main-do/419185#419185
'''
你可能自然会想，为什么有人会想要这样做呢？好吧，有时你想写一个.py文件，
它既可以被其他程序和/或模块作为模块使用，又可以被其他程序和/或模块使用。
'''
print("before import")
import math

print("before functionA")
def functionA():
    print("Function A")

print("before functionB")
def functionB():
    print("Function B {}".format(math.sqrt(100)))

print("before __name__ guard")
if __name__ == '__main__':
    functionA()
    functionB()
print("after __name__ guard")

