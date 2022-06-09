'''
https://www.codewars.com/kata/5bf774a81505a7413400006a/train/python

input:
"hello. my name is inigo montoya. you killed my father. prepare to die."

output:
"Hello. My name is inigo montoya. You killed my father. Prepare to die."
'''
paragraph = "hello. my name is inigo montoya. you killed my father. prepare to die."

def fix(paragraph):
    print(paragraph.split('. '))  # space
    ans = map(lambda x:x.capitalize(), paragraph.split('. '))
    return '. '.join(ans)
print(fix(paragraph))


#1st solution
def fix(paragraph):
    p = paragraph.split('. ')
    return '. '.join(i.capitalize() for i in p)


def fix(paragraph):
    ans = [word.capitalize() for word in paragraph.split('.')]
    return '.'.join(ans)
print(fix(paragraph))

# Be attention title() is diff with capitalize()
def fix(paragraph):
    ans = [word.title() for word in paragraph.split('.')]
    return ''.join(ans)+'.'
