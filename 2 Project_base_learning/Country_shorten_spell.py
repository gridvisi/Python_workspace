
'''
https://pypi.org/project/num2words/
lang: The language in which to convert the number. Supported values are:

en (English, default)
ar (Arabic)
cz (Czech)
de (German)
dk (Danish)
en_GB (English - Great Britain)
en_IN (English - India)
es (Spanish)
es_CO (Spanish - Colombia)
es_VE (Spanish - Venezuela)
eu (EURO)
fi (Finnish)
fr (French)
fr_CH (French - Switzerland)
fr_BE (French - Belgium)
fr_DZ (French - Algeria)
he (Hebrew)
id (Indonesian)
it (Italian)
ja (Japanese)
kn (Kannada)
ko (Korean)
lt (Lithuanian)
lv (Latvian)
no (Norwegian)
pl (Polish)
pt (Portuguese)
pt_BR (Portuguese - Brazilian)
sl (Slovene)
sr (Serbian)
ro (Romanian)
ru (Russian)
sl (Slovene)
tr (Turkish)
th (Thai)
vi (Vietnamese)
nl (Dutch)
uk (Ukrainian)
'''
import re
from num2words import num2words

ordinalAsNumber = "1000000000000nd"
number = re.search('\d+', ordinalAsNumber)
ordinalAsString = num2words(number[0], ordinal=True)
print( ordinalAsString ) # forty-second