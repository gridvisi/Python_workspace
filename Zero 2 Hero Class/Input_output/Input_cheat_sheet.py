
name = input("Enter name: ")
age = input("Enter age: ")

print("data_type of name: ", type(name))
print("data_type of age: ", type(age))

# print sum of two numbers taken from the user

num_1 = int(input("Enter first num: "))
num_2 = int(input("Enter second num: "))

print('Type of num_1:',type(num_1))
print('Type of num_2:',type(num_2))

result = num_1 + num_2
print("The sum of given numbers is : ", result)

#同时输入三个描述：name，age，score
name, age, score = input("Enter student's name, age and score separated by space:").split()
print("Student Name:", name)
print("Student Age:", age)
print("Student Score:", score)


entered_list = input("Enter a list of numbers separated by space: ").split()
print('Intermediate_list: ',entered_list)

num_list = list(map(int,entered_list))
print('Number List: ',num_list)
print('List sum:', sum(num_list))


float_1 = float(input("Enter value: "))
print('Type of float_1:',type(float_1))

result = float_1*2
print("Twice the given numbers is : ", result)


try:
    num = int(input('Enter a number: '))
    print('Good job. The entered number is: ', num)

except ValueError:
    print('This is not a number.')

while True:
    try:
        num = int(input('Enter a number: '))
        break

    except ValueError:
        print('Invalid Input. Try again.')

print('Good job. The entered number is: ', num)



total_input = []
print("Enter Student Names: ")

while True:
    name = input()
    if name:
        total_input.append(name)
    else:
        break

print('Total input received :')
print(total_input)

#User Input


name = input("Hello, who are you? ")

print(f"Hello, {name}, it's so nice to have you in class!")

# Getting two pieces of input.
first_name = input("Hi, what's your first name? ")
last_name = input("Hi, what's your last name? ")
print(f"Hello, {first_name} {last_name}!")
