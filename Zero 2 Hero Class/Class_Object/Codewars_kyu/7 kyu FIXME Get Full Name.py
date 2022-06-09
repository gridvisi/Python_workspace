'''
https://www.codewars.com/kata/597c684822bc9388f600010f/train/python

The code provided is supposed return a person's Full Name given their first and last names.

But it's not working properly.

Notes
The first and/or last names are never null, but may be empty.

Task
Fix the bug so we can all go home early.


import codewars_test as test
from preloaded import *
from solution import Dinglemouse

@test.describe("Basic Tests")
def fixed_tests():
    @test.it('Sample Test Cases')
    def sample_test_cases():
        test.assert_equals(Dinglemouse('Clint', 'Eastwood').get_full_name(), 'Clint Eastwood')
        test.assert_equals(Dinglemouse('', 'Eastwood').get_full_name(), 'Eastwood')
        test.assert_equals(Dinglemouse('Clint', '').get_full_name(), 'Clint')
        test.assert_equals(Dinglemouse('', '').get_full_name(), '')
'''
# solve by ericlee
class Dinglemouse():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def get_full_name(self):
        space = (len(self.first_name) * len(self.last_name) != 0)
        return self.first_name + space*" " +self.last_name

#1st
class Dinglemouse(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def get_full_name(self):
        return (self.first_name + ' ' + self.last_name).strip()

#2nd
class Dinglemouse(object):
    def __init__(self, first, last):
        self.name = '{} {}'.format(first, last).strip()
    def get_full_name(self):
        return self.name

#3rd
class Dinglemouse(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'.strip()



# extend scope of Class_usage
class Dinglemouse(object):
    def __init__(self, first_name, last_name):
        first_name = first_name
        last_name = last_name
    def get_full_name(self):
        return self.first_name + ' ' + self.last_name
Dinglemouse.first_name = 'Clint'
Dinglemouse.last_name = 'Eastwood'
x = Dinglemouse('Clint','Eastwood')
print(Dinglemouse.first_name)
print(Dinglemouse.get_full_name)

class Dinglemouse:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def get_full_name(self):
        return self.first_name + ' ' + self.last_name
print(''.join(["*" for i in range(60)]))
x = Dinglemouse
x.first_name = 'clint'
x.last_name = 'Eastwood'
print(x.get_full_name)
print(x)


class Dinglemouse:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

print(''.join(["*" for _ in range(60)]))
x = Dinglemouse
x.first_name = 'clint'
x.last_name = 'Eastwood'
print(x.get_full_name)
print(x)

