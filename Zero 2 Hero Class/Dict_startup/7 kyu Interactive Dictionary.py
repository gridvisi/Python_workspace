'''
https://www.codewars.com/kata/57a93f93bb9944516d0000c1/train/python

d = Dictionary()

d.newentry("Apple", "A fruit")
test.assert_equals(d.look("Apple"), "A fruit")

d.newentry("Soccer", "A sport")
test.assert_equals(d.look("Soccer"), "A sport")
test.assert_equals(d.look("Hi"), "Can't find entry for Hi")
test.assert_equals(d.look("Ball"), "Can't find entry for Ball")

d.newentry("soccer", "a sport")
test.assert_equals(d.look("soccer"), "a sport")

class Dictionary():
    def __init__(self):
        # Your code

    def newentry(self, word, definition):
        # Your code

    def look(self, key):
        # your code
'''


class Dictionary(object):
    def __init__(self):
        self.my_dict = {}

    def look(self, key):
        return self.my_dict.get(key, "Can't find entry for {}".format(key))

    def newentry(self, key, value):
        """ new_entry == PEP8 (forced by Codewars) """
        self.my_dict[key] = value
# your code

class Dictionary(dict):
    newentry = dict.__setitem__

    def look(self, key):
        return self.get(key, f"Can't find entry for {key}")

class Dictionary(dict):
    def newentry(self, word, definition):
        self[word] = definition
    def look(self, key):
        return self[key] if key in self else "Can't find entry for " + key


class Dictionary():
    def __init__(self):
        self.db = {}

    def newentry(self, word, definition):
        self.db[word] = definition

    def look(self, key):
        return self.db.get(key, f'Can\'t find entry for {key}')