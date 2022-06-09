'''
https://www.codewars.com/kata/53369039d7ab3ac506000467/train/python
'''

start = 0
for i in range(11):
    start = i + start
print(start)


def bool_to_word(boolean):
    return {'Yes':True,'No':False}[boolean]

def bool_to_word(bool):
    return "Yes" if bool else "No"

def bool_to_word(bool):
    return ['No', 'Yes'][bool]

bool_to_word = {True: 'Yes', False: 'No'}.get