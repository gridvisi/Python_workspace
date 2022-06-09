'''
https://www.codewars.com/kata/582e0e592029ea10530009ce/train/python

The objective of Duck, duck, goose is to walk in a circle, tapping
on each player's head until one is chosen.

Task: Given an array of Player objects (an array of associative
arrays in PHP) and an index (1-based), return the name of the
chosen Player(name is a property of Player objects, e.g Player.name)

Example:

duck_duck_goose([a, b, c, d], 1) should return a.name
duck_duck_goose([a, b, c, d], 5) should return a.name
duck_duck_goose([a, b, c, d], 4) should return d.name


test.describe("fixed tests")
test.it("should find the correct goose")
test.assert_equals(duck_duck_goose(players, 1),  "a")
test.assert_equals(duck_duck_goose(players, 3),  "c")
test.assert_equals(duck_duck_goose(players, 10), "z")
test.assert_equals(duck_duck_goose(players, 20), "z")
test.assert_equals(duck_duck_goose(players, 30), "z")
test.assert_equals(duck_duck_goose(players, 18), "g")
test.assert_equals(duck_duck_goose(players, 28), "g")
test.assert_equals(duck_duck_goose(players, 12), "b")
test.assert_equals(duck_duck_goose(players, 2),  "b")
test.assert_equals(duck_duck_goose(players, 7),  "f")
'''

def duck_duck_goose(players, goose):
    return players[(goose % len(players)) - 1].name

players, goose = ['a', 'b', 'c', 'd'], 4  # "z"
print(duck_duck_goose(players,goose))