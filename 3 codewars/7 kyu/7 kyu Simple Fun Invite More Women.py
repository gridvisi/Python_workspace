'''

Task
King Arthur and his knights are having a New Years party. Last year Lancelot was jealous of Arthur, because Arthur had a date and Lancelot did not, and they started a duel.

To prevent this from happening again, Arthur wants to make sure that there are at least as many women as men at this year's party. He gave you a list of integers of all the party goers.

Arthur needs you to return true if he needs to invite more women or false if he is all set.

Input/Output
[input] integer array L ($a in PHP)

An array (guaranteed non-associative in PHP) representing the genders of the attendees, where -1 represents women and 1 represents men.
2 <= L.length <= 50
[output] a boolean value

true if Arthur need to invite more women, false otherwise.

Test.assert_equals(invite_more_women([1, -1, 1]),True)
Test.assert_equals(invite_more_women([-1, -1, -1]),False)
Test.assert_equals(invite_more_women([1, -1]),False)
Test.assert_equals(invite_more_women([1, 1, 1]),True)
Test.assert_equals(invite_more_women([]),False)

PUZZLESGAMES
'''

def invite_more_women(arr):
    return sum(arr) > 0

def invite_more_women(arr):
    x = arr.count(-1)
    y = arr.count(1)
    if x >= y:
        return 0
    else:
        return 1

def invite_more_women(arr):
    return arr.count(1) > arr.count(-1)

def invite_more_women(arr):  #mcree
    sum = 0
    for i in arr:
        sum += i
    return sum > 0