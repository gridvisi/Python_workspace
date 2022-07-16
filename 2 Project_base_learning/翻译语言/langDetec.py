
'''
pip install langdetect
'''

from langdetect import detect

text = "you come from british"
print(detect(text))

text = "Ciao,Questa è la vita"
print(detect(text))

text = "C'est la vie"
print(detect(text))


