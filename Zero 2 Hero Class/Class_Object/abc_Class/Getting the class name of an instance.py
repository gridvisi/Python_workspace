
import itertools
x = itertools.count(0)
print(type(x).__name__)
'count'

class A:
    @classmethod
    def get_classname(cls):
        return cls.__name__

    def use_classname(self):
        return self.get_classname()
#Usage:

A.get_classname()
'A'
a = A()
print(a.get_classname())
'A'
print(a.use_classname())
'A'

class person(object):
    def __init__(self,name):
        self.name = name
    #@classmethod
    #@property
    #@staticmethod
    def info(self):
        print ("My name is {0}, I am a {1}".format(self.name,self.__class__.__name__))
        return ("My name is {0}, I am a {1}".format(self.name, self.__class__.__name__))
#bob = person(name = 'Robert')

person.name = 'Robert'
Bob = person(name = 'robert')
#Bob = person.info()
print(Bob.name)
print(Bob.info())
"My name is Robert, I am a person"

#3 follow up #2
# add_on argum in info

class Person(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
    #@classmethod
    #@property
    #@staticmethod
    def info(self,gender):
        #print ("My name is {0}, I am a {1}".format(self.name,self.__class__.__name__))
        #print(gender)
        g = (gender == self.gender)
        return (f"{g} My name is {self.name}, I am a {self.gender}, {self.__class__.__name__}")
#bob = person(name = 'Robert')

#Person.name = 'Robert'
ada = Person
ada = Person(name = 'alex',gender = 'female')

print(ada.name)
print(ada.info('male'))
"My name is Robert, I am a person"