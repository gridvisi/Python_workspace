'''
https://www.codewars.com/kata/6089c7992df556001253ba7d/train/python

Your job is to create a class called Song.

A new Song will take two parameters, title and artist.

mount_moose = Song('Mount Moose', 'The Snazzy Moose')

mount_moose.title => 'Mount Moose'
mount_moose.artist => 'The Snazzy Moose'
You will also have to create an instance method named howMany() (or how_many()).

The method takes an array of people who have listened to the song that day.
The output should be how many new listeners the song gained on that day out of
all listeners. Names should be treated in a case-insensitive manner, i.e.
"John" is the same as "john".

Example
mount_moose = Song('Mount Moose', 'The Snazzy Moose')

# day 1 (or test 1)
mount_moose.how_many(['John', 'Fred', 'BOb', 'carl', 'RyAn']) => 5
# These are all new since they are the first listeners.

# day 2
mount_moose.how_many(['JoHn', 'Luke', 'AmAndA']); => 2
# Luke and Amanda are new, john already listened to it the previous day
Also if the same person listened to it more than once a day it should only count them once.

Example
mount_moose = Song('Mount Moose', 'The Snazzy Moose')

# day 1
mount_moose.how_many(['John', 'joHN', 'carl']) => 2
Good luck!

FUNDAMENTALSCLASSESBASIC LANGUAGE FEATURESOBJECT-ORIENTED PROGRAMMING
'''

#1st
class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self._seen = set()

    def how_many(self, people):
        tmp = set(map(str.lower, people))
        res = len(tmp - self._seen)
        self._seen.update(tmp)
        return res


class Song:
    audience = []
    def __init__(self,title,artist,listen):
        self.title = title
        self.artist = artist
        self.listen = listen
    def how_many(self):
        return len(self.listen)

    def howMany(self):
        self.audience.append(self.listen)
        return self.audience #[i for i in self.listen if i not in self.listen]

s = Song('a','b',['1','2'])
s.listen = ['John', 'Fred', 'BOb', 'carl', 'RyAn']
print(s.listen)

s.title = 'Mount Moose'
s.artist = 'The Snazzy Moose'

print(s.how_many())

print(s.listen)
for name in ['John', 'Fred', 'BOb', 'carl', 'RyAn']:
    s.listen = name
    s.howMany()
print(s.howMany())




# 2nd solution is Not correct

class Song:
    def __init__(self,name):
        self.name = name

    def howMany(self,person):
        return person #[i for i in self.listen if i not in self.listen]

#TypeError: __init__() takes 2 positional arguments but 4 were given
#s = Song('Mount Moose','The Snazzy Moose',['John', 'Fred', 'BOb', 'carl', 'RyAn'])

#case = Song('Mount Moose','The Snazzy Moose',['John', 'Fred', 'BOb', 'carl', 'RyAn'])
case = Song
case.title = 'Mount Moose'
case.artist = 'The Snazzy Moose'
case.person = ['John', 'Fred', 'BOb', 'carl', 'RyAn']
#person = ['John', 'Fred', 'BOb', 'carl', 'RyAn']
#print(s.listen)
#print(case.howMany)


#Case study
class Person:
    def __init__(self, name, job=None, pay=10):
        self.name = name
        self.job = job
        self.pay = pay

    def getRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
        return self.pay


p = Person("xiaoming", "jixie")
print(p.getRaise(0.8))  # output:18
