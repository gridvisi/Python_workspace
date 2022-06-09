# xing shi code [1,2,3, ... ...]

#1
answer = 0
for i in range(100):
    if i%2 == 1:
        answer += i
print(answer)
#2
print(sum([i for i in range(100) if i%2==1]))

#3
#print(sum(range(100) if i%2==1))
print(sum(range(99)[1:99:2]))  #2401
print(list(range(100))[1::2])
print(sum(list(range(100))[1::2]))

# + - * / %
print(4%2, 10%3, 100%99)
print(4//2, 10//3, 100//99)
print(10//3)
print(10/3)

# FEIFEI IS GIRL == True
# hongyu is girl == False
print('False + 1:',False + 1)

print(0 == False, 1 == True)
#if x % 3:


for i in range(365):
    if i%3 and i%5 == 0:
        print(i)
        print('i%3:',i%3)



#
print(sum([i for i in range(11)]))

print(1+2)

print([1,2])

# ear：A, head：B，glasses：C


#if teacher_li see and xing is laughing

#if coffee is hot:
#    print("do not drink")
#else:
#    if coffee is not ice
#     if coffee is not posion
#    print("do drink")

'''
if light == red:
    car stop
if  light == green:
    car go through
if light == yellow:
    depend on

'''

'''
https://www.codewars.com/kata/53dc23c68a0c93699800041d/train/python

test.assert_equals(smash(["hello"]), "hello")
test.assert_equals(smash(["hello", "world"]), "hello world")
'''
print(3%2,9%3,100%9)

start = 0
end = 10

result = 0
for x in range(start,end+1):
    if x%2 == 0:
        result += x
print('start:end',result)


text = "I like hotspot and eat every week"

result = ""
for x in text:
    if x == " ":
        x = ""
        result += x
print(result)


shuru = ["hello", "world"]
shuchu = "hello world"

print("hello " + "world")


def smash(words):
    return words