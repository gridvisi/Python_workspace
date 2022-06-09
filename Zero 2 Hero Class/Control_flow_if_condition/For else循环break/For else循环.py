#example:
leaders = ["Elon", "Tim", "Warren"]

for i in leaders:
    if i == "Yang":
        print("Yang is a leader!")
    break
else:
    print("Not found Yang!")

# Not found Yang!

leaders = ["Yang", "Elon", "Tim", "Warren"]

for i in leaders:
    if i == "Yang":
        print("Yang is a leader!")
    break
else:
    print("Not found Yang!")

# Yang is a leader!


leaders = ["Yang", "Elon", "Tim", "Warren"]

for i in leaders:
    if i == "Yang":
        have_yang = True
    # Do something
    break
else:  # no yang
    ...  # Do others

#nest loop
leaders = [("Yang",45), ("Elon", 50),("Tim",58),
           ("Yang",47),("Warren",60)]

target = ["Yang","male",47]
for i in leaders:
    for j in i:
        if j in target and i in target:
            print(f"1:the {i} who's {j} years old exist")
            break
        if not (j in target and i in target):
            continue
    #break
    print(f"2:the the {i} who's {j} years old not exist")

# For_else solution
target = ("Yang","male",47)
for i in leaders:
    for j in i:
        print(j,i)
        if j in target and i in target:
            print(f"3:the {i} who's {j} years old exist")
    #break
else:
    #continue
    print(f"4:the {i[0]} who's {j} years old not exist")
#break
#print(f"5:the {i[0]} who's {j} years old exist")


# Orignal
for i in range(5):
    for j in range(5):
        if j == 2 and i == 0:

            break
        if not (j == 2 and i == 0):
            continue
    break

# use the for-else syntax
for i in range(5):
    for j in range(5):
        if j == 2 and i == 0:
            break
    else:  # only execute when it's no break in the inner loop
        continue
    break

nums = [1, 3, 0, 5]

for denominator in nums:
    try:
        20 / denominator
    except ZeroDivisionError:
        break

else:  # no found ZeroDivisionError
    ...  # Do others

fruit = ['apple','carrot','banana']

for i in fruit:
    if i == 'Pycharm':
        print(f"{i} in fruit")
print("Pycharm not in fruit")
#else:print(f"Pycharm not in fruit")

for i in range(5):
    for j in range(5):
        if j == 2 and i == 0:
            break
    else:  # only execute when it's no break in the inner loop
        continue
    break


# Origin 8*8 单位为1*1的格子方阵，从0，0 到(3，5)有多少种走法？
cunt = 0
path = []
i,j = 0,0

while True:
    if (i,j) not in path:
        path.append((i,j))
        if i < 3 and j < 5:
            i += 1
    elif i==3 and j == 5:
        print('path:',path)
    j += 1
    break

for i in range(9):
    if (i, j) not in path and (i <= 3 and j <= 5):
        path.append([i, j])
    for j in range(9):
        if (i,j) not in path and (i<=3 and j<=5):
            path.append([i,j])

            if j == 3 and i == 5:
                path.append(';')


    #continue
    #break
print('path_cunt:',path)

# Origin 4*6 单位为1*1的格子方阵，从0，0 到(4，6)有多少种走法？
cunt = 0
for i in range(9):
    for j in range(9):
        #if j == 3 and i == 5:
        if j + i == 3+5:
            cunt += 1
            #break
        if not (j + i == 3+5):
            continue
    #break
print('cunt:',cunt)