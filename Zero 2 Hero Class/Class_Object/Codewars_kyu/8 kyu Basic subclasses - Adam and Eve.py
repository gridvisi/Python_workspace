'''
https://www.codewars.com/kata/547274e24481cfc469000416/train/python

According to the creation myths of the Abrahamic religions, Adam and Eve were the
first Humans to wander the Earth.

You have to do God's job.
The creation method must return an array of length 2 containing objects
(representing Adam and Eve).

The first object in the array should be an instance of the class Man.
The second should be an instance of the class Woman.
Both objects have to be subclasses of Human.
Your job is to implement the Human, Man and Woman classes.

paradise = God()
test.assert_equals(isinstance(paradise[0], Man) , True, "First object are a man")
'''

class God():
    def __init__(self,human):
        self.man = human[0]
        self.woman = human[1]
        self.human = human
    def isinstance(self):
        return self.human[0] == 'Man' and self.human[1] == 'Woman'

    def isMan(self):
        return self.human[0] == 'Man'

    def isWoman(self):
        return self.human[1] == 'woman'

paradise = God
paradise.human = ['man','woman']


#1st
def God():
    return [Man(), Woman()]

class Human(object):
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

#3
def God():
    return [ Man("Adam"), Woman("Eva") ]

class Human:
   def __init__( self, name ):
      self.name = name

class Man( Human ):
   def __init__( self, name ):
      self.name = name

class Woman( Human ):
   def __init__( self, name ):
      self.name = name

paradise = God()
print(isinstance(paradise[0],Man))
print(isinstance(paradise[0],Woman))
print(isinstance(1,int))