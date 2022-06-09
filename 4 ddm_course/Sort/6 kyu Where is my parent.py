'''
https://www.codewars.com/kata/58539230879867a8cd00011c/python
Mothers arranged a dance party for the children in school. At that party,
there are only mothers and their children.
All are having great fun on the dance floor when suddenly all the lights went out.
It's a dark night and no one can see each other.
But you were flying nearby and you can see in the dark and have ability to teleport people
anywhere you want.

Legend:
-Uppercase letters stands for mothers, lowercase stand for their children,
i.e. "A" mother's children are "aaaa".
-Function input: String contains only letters, uppercase letters are unique.
Task:
Place all people in alphabetical order where Mothers are followed by their children,
 i.e. "aAbaBb" => "AaaBbb".
'''
dancing_brigade = "aAbaBb"
print(sorted(dancing_brigade))

def find_children(s):
    return ''.join(sorted(sorted(s),key=str.upper))
s = "aAbaBb"
print(find_children(s))

'''

def find_children(dancing_brigade):
    d = sorted(dancing_brigade)
    print(d)
    key = [i for i in sorted(d) if i.isupper()]
    return [x.upper() for x in sorted(d) for x in key]
dancing_brigade = "xXfuUuuF"
print('1',find_children(dancing_brigade))
'''

def find_children(s):
    return ''.join( sorted(sorted(s), key=str.lower) )