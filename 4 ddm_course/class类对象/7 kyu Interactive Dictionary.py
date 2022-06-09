# https://www.codewars.com/kata/57a93f93bb9944516d0000c1/train/python
'''
d = Dictionary()
d.newentry('Apple', 'A fruit that grows on trees')
print(d.look('Apple'))
A fruit that grows on trees
print(d.look('Banana'))
Can't find entry for Banana
'''
class Dictionary():
    def __init__(self):
        self.word = []
        self.definition = []
        self.key = None

    def newentry(self, word, definition):
        self.word += [word]
        self.definition += [definition]
        #print(self.word.index(word))
        return self.definition[self.word.index(word)]

    def look(self, key):
        if key in self.word:
            return self.definition
        else:
            return "Can't find entry for " + f"{key}"


# Top 1st
class Dictionary(object):
    def __init__(self):
        self.my_dict = {}

    def look(self, key):
        return self.my_dict.get(key, "Can't find entry for {}".format(key))

    def newentry(self, key, value):
        """ new_entry == PEP8 (forced by Codewars) """
        self.my_dict[key] = value

d = Dictionary()
d.newentry('Apple', 'A fruit that grows on trees')
d.newentry('carrot', 'A fruit that grows under earth')
print(d.look('Apple'))
print(d.look('Banana'))
print(d.word)

# 2nd Solution
class Dictionary(dict):
    newentry = dict.__setitem__

    def look(self, key):
        return self.get(key, f"Can't find entry for {key}")

# 3rd Solution
class Dictionary():
    def __init__(self):
        self.d = {}
    def newentry(self, word, definition):
        self.d[word]=definition
    def look(self, key):
        return self.d.get(key) or "Can't find entry for {}".format(key)

# 4th Solution
class Dictionary(dict):
    def newentry(self, word, definition):
        self[word] = definition
    def look(self, key):
        return self[key] if key in self else "Can't find entry for " + key

# Sample code
class Box:
    def setDimension(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def getVolume(self):
        return self.width * self.height * self.depth

b = Box()
b.setDimension(10, 20, 30)
