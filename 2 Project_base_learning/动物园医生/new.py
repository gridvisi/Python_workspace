#Creating our animal park

animal_park = ['Rabbit','Rabbit','Rabbit','Rabbit',
'Cat','Cat','Cat','Cat','Cat','Cat','Cat',
'Turtle','Turtle','Turtle','Turtle','Turtle','Turtle','Turtle',
'Dog','Dog',
'Kangaroo','Kangaroo','Kangaroo','Kangaroo','Kangaroo','Kangaroo']

#现在你的任务是穿过动物公园，一个一个地挑选动物。将需要检查的动物放入一个新的数组。
#注意受试者是除去猫和狗以外的所又动物，放入animal_doctor
#Creating a new list for our animal doctor with all animals

animal_doctor = []
for animal in animal_park:
    print('ceshi:', animal_doctor)
    animal_doctor.append(animal) # 运行代码应该看到数组里没有猫和狗
print('ceshi:', animal_doctor == animal_park)
#print('good! ','zhouhongyu == lizonglin)
print('do you have passport for check in')

