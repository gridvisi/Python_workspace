#https://stackoverflow.com/questions/56813864/is-there-a-python-function-to-convert-ordinal-number-to-word

#https://pypi.org/project/num2words/

import re
from num2words import num2words

ordinalAsNumber = "42nd"
ordinalAsNumber = "42"
number = re.search('\d+', ordinalAsNumber)
ordinalAsString = num2words(number[0], ordinal=True)
print( ordinalAsString ) # forty-second

text = "Text with several ordinals such as 42nd, 31st, and 5th as well as plain numbers such as 1, 2, 3."
numbers = re.findall('(\d+)[st|nd|rd|th]', text)

for n in numbers:
     ordinalAsString = num2words(n, ordinal=True)
     print( ordinalAsString )


text = "Text with several ordinals such as 42nd, 31st, and 5th as well as plain numbers such as 1, 2, 3."
numbers = re.findall('(\d+)[st|nd|rd|th]', text)

newText = text
for n in numbers:
     ordinalAsString = num2words(n, ordinal=True)
     newText=re.sub(r"\d+[st|nd|rd|th]", ordinalAsString, text, 1)

print ( text )
print( newText )