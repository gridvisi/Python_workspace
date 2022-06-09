
def squares(x=0):
    while x < 10:
        x = x + 1
        yield x*x

for i in squares():
    print(i,end=",")


def generator_func():
  num = 1
  print("First time execution of the function")
  yield num
  num = 10
  print("Second time execution of the function")
  yield num
  num = 100
  print("Third time execution of the function")
  yield num

obj = generator_func()


def cubicvar():
    i = 1
    while True:
        yield i * i * i

        i += 1


for num in cubicvar():
    if num > 1000:
        break
    print(num,end=",")

'''
练习二：写一个流水线多个生成器接力返回奇数的程序。
多个生成器可以通过管道化,一个生成器使用另一个生成器），
作为同一代码中的一系列操作。管道化还可以使代码更加高效和易读。​
管道化的函数，使用()paranthesis在函数内部给出函数调用者。
'''
def gen_int(n):
    for i in range(n):
        yield i

def gen_2(gen):
    for n in gen:
        if n % 2:
            yield n

for i in gen_2(gen_int(10)):
    print(i)