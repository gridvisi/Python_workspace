'''
https://www.codewars.com/kata/the-hashtag-generator/solutions/python

The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
Examples
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
ALGORITHMSSTRINGS
'''

def generate_hashtag(s):
    ans = '#' + str(s.title().replace(' ',''))
    return s and not len(ans)>140 and ans or False


def generate_hashtag(s):
    output = "#"
    for word in s.split():
        output += word.capitalize()
    return False if (len(s) == 0 or len(output) > 140) else output


def generate_hashtag(s):
    s = s.lower()
    s = list(s)
    if len(s) > 140 or not s:
        return False
    if ord(s[0]) > 96 and ord(s[0]) < 123:
        s[0] = chr(ord(s[0])-32)
    for i in range(len(s)-1):
        if s[i] == ' ':
            if ord(s[i+1]) > 96 and ord(s[i+1]) < 123:
                s[i+1] = chr(ord(s[i+1])-32)
    for i in range(s.count(' ')):
        s.remove(' ')
    s.insert(0,'#')
    return ''.join(s)