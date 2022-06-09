'''
https://www.codewars.com/kata/first-non-repeating-character/solutions/python
Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string.
For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.
As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.
If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.

ALGORITHMSSTRINGSSEARCH
'''


def first_non_repeating_letter(string):
    string_lower = string.lower()
    for i, letter in enumerate(string_lower):
        if string_lower.count(letter) == 1:
            return string[i]

    return ""


def first_non_repeating_letter(string):
    s = string.lower()

    for i in string:
        if s.count(i.lower()) == 1:
            return i
    return ''

def first_non_repeating_letter(string):
    backup = string
    string = string.lower()
    backup = list(backup)
    string = list(string)
    if not string:
        return ''
    for i in range(len(string)):
        if string.count(string[i]) == 1:
            return str(backup[i])
    return ''