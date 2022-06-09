'''
https://www.codewars.com/kata/5b1d1812b6989d61bd00004f/train/python

string = "This is an example. Return the nth occurrence of example in this example string."
find_nth_occurrence("example", string, 1) == 11
find_nth_occurrence("example", string, 2) == 49
find_nth_occurrence("example", string, 3) == 65
find_nth_occurrence("example", string, 4) == -1
'''
string = "This is an example. Return the nth occurrence of example in this example string."
substring = 'example'

def find_nth_occurrence(substring, string, occurrence=3):
    s = 0
    for i in range(occurrence):
        #print(string[s:], s)
        index = string[s:].find(substring)
        if index == -1:
            return -1
        else:
            s += index + len(substring)
            #string = string[s:]

    return s - len(substring)
print(find_nth_occurrence(substring, string, occurrence=3))