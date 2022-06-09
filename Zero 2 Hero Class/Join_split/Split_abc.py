'''
https://www.codewars.com/kata/5f77d62851f6bc0033616bd8/solutions/python

'Hello world' = True
' Hello world' = False
'Hello world  ' = False
'Hello  world' = False
'Hello' = True
# Even though there are no spaces, it is still valid because none are needed
'Helloworld' = True
# True because we are not checking for the validity of words.
' ' = False
'' = True
'''

def valid_spacing(s):
    return s == ' '.join(s.split())


'''
Which of the following would separate a string input_string on the 
first 2 occurences of the letter “e”?
以下哪种情况会使一个字符串input_string的前两次出现的字母 "e "分开？
'''
input_string = "occurences"

print('e'.split(input_string, maxsplit=2))
print(input_string.split('e', 2))
#Incorrect

print('e'.split(input_string, 2))
print(input_string.split('e', maxsplit=2))


