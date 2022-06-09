'''
https://www.codewars.com/kata/5effa412233ac3002a9e471d/train/python

@test.it("Actual Addition")
def real_addition_test():
    test.assert_equals(add(2,11), 13)
    test.assert_equals(add(0,1), 1)
    test.assert_equals(add(0,0), 0)

@test.it("Silly Addition")
def silly_addition_test():
    test.assert_equals(add(16,18), 214)
    test.assert_equals(add(26,39), 515)
    test.assert_equals(add(122,81), 1103)

'''
#2nd solution by ericlee

num1, num2 = 122,81  # 1103
def add(num1, num2):
    if num1 <= num2: num1,num2 = num2,num1
    numS1,numS2 = map(str,[num1,num2])
    #if str(num1) == max(map(str,[num1,num2]),key=len):
    numS2 = (len(numS1) - len(numS2))*'0' + numS2

    return int(''.join([str(int(x)+int(y)) for x,y in zip(numS1,numS2)]))

num1, num2 = 0,1
print(add(num1,num2))

#1st solution
def add(a,b):
    s = ""
    while a+b:
        a,p = divmod(a,10)
        b,q = divmod(b,10)
        s = str(p+q)+s
    return int(s or'0')

#2 solution
def add(*args):
    a, b = map(str, sorted(args))
    a = a.zfill(len(b))
    result = [int(x) + int(y) for x, y in zip(a, b)]
    return int("".join(map(str, result)))

#3rd solution
def add(a,b):
    return int(str(add(a//10,b//10))+str(a%10+b%10)) if a*b else a+b

#5th solution
def add(num1, num2):
    result = ""
    while num1 or num2:
        result = f"{num1 % 10 + num2 % 10}{result}"
        num1, num2 = num1 // 10, num2 // 10
    return int(result or 0)

def add(x, y):
    res = 0
    m = 1
    while x != 0 or y != 0:
        s = x % 10 + y % 10
        res += s * m
        m *= 10 if s < 10 else 100
        x //= 10
        y //= 10
    return res

def add(a, b):
    return int(''.join([str(sum(map(int, item))) for item in
                            zip(str(a).zfill(max(len(str(a)), len(str(b)))),
                                str(b).zfill(max(len(str(a)), len(str(b)))))]))

