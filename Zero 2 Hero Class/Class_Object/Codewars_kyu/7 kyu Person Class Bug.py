'''
https://www.codewars.com/kata/513f887e484edf3eb3000001/train/python

matz = Person('Yukihiro', 'Matsumoto', 47)
test.assert_equals(matz.full_name, 'Yukihiro Matsumoto')
test.assert_equals(matz.age, 47)

joe = Person('Joe', 'Smith', 30)
test.assert_equals(joe.full_name, 'Joe Smith')
test.assert_equals(joe.age, 30)
'''


class Person():

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return self.first_name +" " + self.last_name


#1st
class Person():

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


#2nd
class Person():

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f"{first_name} {last_name}"
        self.age = age

p = Person
#print(p('Yukihiro', 'Matsumoto', 47).full_name())
p = Person('Yukihiro', 'Matsumoto', 47)
print(p.full_name)