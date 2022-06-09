'''
https://www.codewars.com/kata/5a86073fb17101e453000258/train/python

You'll have a function called "sortEmotions" that will return an array of emotions sorted. It has two parameters, the first parameter called "arr" will expect an array of emotions where an emotion will be one of the following:

:D -> Super Happy
:) -> Happy
:| -> Normal
:( -> Sad
T_T -> Super Sad
Example of the array:[ 'T_T', ':D', ':|', ':)', ':(' ]

And the second parameter is called "order", if this parameter is true then the order of the emotions will be descending (from Super Happy to Super Sad) if it's false then it will be ascending (from Super Sad to Super Happy)

Example if order is true with the above array: [ ':D', ':)', ':|', ':(', 'T_T' ]

Super Happy -> Happy -> Normal -> Sad -> Super Sad
If order is false: [ 'T_T', ':(', ':|', ':)', ':D' ]

Super Sad -> Sad -> Normal -> Happy -> Super Happy
Example:

arr = [':D', ':|', ':)', ':(', ':D']
sortEmotions(arr, true) // [ ':D', ':D', ':)', ':|', ':(' ]
sortEmotions(arr, false) // [ ':(', ':|', ':)', ':D', ':D' ]
More in test cases!

Notes:

The array could be empty, in that case return the same empty array ¯\_( ツ )_/¯
All emotions will be valid


test.describe("Basic Tests")

test.it("Descending")
test.assert_equals(sort_emotions([ ':D', 'T_T', ':D', ':(' ], True), [ ':D', ':D', ':(', 'T_T' ])
test.assert_equals(sort_emotions([ 'T_T', ':D', ':(', ':(' ], True), [ ':D', ':(', ':(', 'T_T' ])
test.assert_equals(sort_emotions([ ':)', 'T_T', ':)', ':D', ':D' ], True), [ ':D', ':D', ':)', ':)', 'T_T' ])

test.it("Ascending")
test.assert_equals(sort_emotions([ ':D', 'T_T', ':D', ':(' ], False), [ 'T_T', ':(', ':D', ':D' ])
test.assert_equals(sort_emotions([ 'T_T', ':D', ':(', ':(' ], False), [ 'T_T', ':(', ':(', ':D' ])
test.assert_equals(sort_emotions([ ':)', 'T_T', ':)', ':D', ':D' ], False),  [ 'T_T', ':)', ':)', ':D', ':D' ])

test.it("Empty array")
test.assert_equals(sort_emotions([], False), [])
test.assert_equals(sort_emotions([], True), [])
'''

def sort_emotions(arr, order):
    # (ง •̀_•́)ง
    emotions = ['T_T', ':(', ':|', ':)', ':D']
    return sorted(arr,key=lambda x:emotions.index(x),reverse= order)

arr,order = [ ':D', 'T_T', ':D', ':(' ],False
print(sort_emotions(arr, order))

#1st
def sort_emotions(arr, order):
    return sorted(arr, key=[':D',':)',':|',':(','T_T'].index, reverse=not order)


#2nd
def get_face(face):
    faces = { ':D':0, ':)':1, ':|':2, ':(':3, 'T_T':4 }
    return faces[face]

def sort_emotions(arr, order):
    return sorted(arr, key=get_face, reverse= not order)

