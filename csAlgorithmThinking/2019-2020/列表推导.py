
#有一个动物公园里面有不同的动物。每年每只动物都需要接受动物医生的检查。你现在就是动物的医生，
# 动物公园花名册按放在数组animal_pack里面

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
    animal_doctor.append(animal) # 运行代码应该看到数组里没有猫和狗
print('ceshi:', animal_doctor)

print('do you have passport for check in')


#标准的循环是这样滴：
animal_doctor = []
for animal in animal_park:
      if animal != 'Dog' and animal != 'Cat':
       animal_doctor.append(animal)

# Python List Comprehension 条件语句是这样滴
#在很多情况下，我们希望使用条件语句。在我们的标准循环中，它可能是这样的：
#如同学所见，我们必须为条件语句添加另一行代码。也可以这样做

animal_doctor = [animal for animal in animal_park if animal != 'Dog' and animal != 'Cat']
print(animal_doctor)