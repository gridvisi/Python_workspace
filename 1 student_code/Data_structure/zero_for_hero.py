
#Python variables contain Number, Strings, Lists, Tuple, Dictionary


# NUMBER

print("NUMBER")

a = 10

b = 15

c = 20

d = 2.35666

e = 45221112545631

print('a + b + c + d = ',a + b + c + d)

del e # deleted e

#print(e) # exception occurs

# string

print("STRING")

string1 = "Awesome"

print(string1[-1])

print(string1[0:4])

print(string1*3)

print(string1[1:])

# List

print("LIST")

mylist = [45,"hello",7.2,"man cron tab"]

print(mylist[1:4])

print(mylist[-1])

tinylist = [1,2]

print(mylist+tinylist)

print(mylist[2:])

mylist[0]=6

print(mylist)

#TUPLES

print("TUPLES")

mytuple = (7,"dam99",45,"Game developer")

print(mytuple)

#DICTIONARY

print("DICTIONARY")
person = dict(zip(['name', 'job', 'code'],['sriram', 'Game Developer', 452211125]))
print(person.items())
print(person.keys())
#dict_keys(['name', 'job', 'code'])
print(person.values())
#dict_values(['sriram', 'Game Developer', 452211125])