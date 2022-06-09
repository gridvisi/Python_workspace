'''
https://brilliant.org/problems/fibonacci-puzzle/
'''

def fibo(n):
    a = 0
    b = 1
    for i in range(1,n):
        c = b
        b = a+b
        a = c
    return b

a = 1
G = ['0','1','2','3','4','5','6','7','8','9']
while(sorted(set(list(str(fibo(a)))))!=G):
    a = a+1
print(fibo(61))

#2
def goal(n):
    number = str(n)
    for digit in '1234567890':
        if digit not in number:
            return False
    return True
memo = {1:0,2:1}
def fib(n):
    if n in memo:
        return memo[n]
    memo[n] = fib(n-1)+fib(n-2)
    return memo[n]
n = 1
while not goal(fib(n)):
    n += 1
print("Answer:", fib(n))

#3
def fib():
    f0 = 0
    yield f0
    f1 = 1
    yield 1
    while True:
        f0,f1 = f1,f0+f1
        yield f1
digit = set(range(0,10))

for f in fib():
    if set(map(int,list(str(f)))) == digit:
        print(f)
        break