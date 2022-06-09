
class Animal:
    def __init__(self, animal_list):
        self.animals_name = animal_list

animals = Animal(["dog","cat","fish"])
#for animal in animals:
#    print(animal)
#TypeError: 'Animal' object is not iterable

class Animal:
    def __init__(self, animal_list):
        self.animals_name = animal_list

    def __getitem__(self, index):
        return self.animals_name[index]

animals = Animal(["dog","cat","fish"])
for animal in animals:
    print(animal)

#Trait of clean python
class Items:
    def __init__(self, values):
        self._values = list(values)

    def __len__(self):
        return len(self._values)

    def __getitem__(self, item):
        return self._values.__getitem__(item)

values = [1,3,2,5,1,4]
ls = Items(values)
print(ls.__len__())
print(ls.__getitem__(0))

'''
情境管理器
上下文管理器提供了一种模式，我们想要运行一些代码，有前置条件和后置条件，也就是说我们要在某个主操作之前和之后运行一些事情。
'''

fd = open('d:/welcome.txt')
file_object = open('d:/welcome.txt')
try:
    all_the_text = file_object.read()

finally:
    file_object.close()

#An elegant alternative is
with open('d:/welcome.txt') as fd:
    #process_file(fd)
    fd.read()