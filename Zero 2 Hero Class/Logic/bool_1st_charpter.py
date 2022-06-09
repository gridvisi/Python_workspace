
bottle = ['mineral water']
bottles = bottle * 6

person = ['zhouhongyu']

person_list = ['zhouhongyu', 'alex', 'xtr', 'mike', 'henry', 'ada']
students = person_list
print(person not in person_list)

persons = 6
for name in person_list: #0-6
    #print(i)
    if name[0] == 'a':
        print('the first is "a":',name)


person_list.append(person)
person_list.append('alex')
person_list.append('xtr')
person_list.append('mike')
person_list.append('henry')
person_list.append('ada')
print(person_list)
print(bottles)

# All student have a bottle of water?

print(len(person_list) == len(students))