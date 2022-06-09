'''
https://www.codewars.com/kata/5d2d0d34bceae80027bffddb/train/python

The goal of this Kata is to write a function that will receive an array of strings as its single argument, then the strings are each processed and sorted (in desending order) based on the length of the single longest sub-string of contiguous vowels ( aeiouAEIOU ) that may be contained within the string. The strings may contain letters, numbers, special characters, uppercase, lowercase, whitespace, and there may be (often will be) multiple sub-strings of contiguous vowels. We are only interested in the single longest sub-string of vowels within each string, in the input array.

Example:

str1 = "what a beautiful day today"
str2 = "it's okay, but very breezy"
When the strings are sorted, str1 will be first as its longest sub-string of contiguous vowels "eau" is of length 3, while str2 has as its longest sub-string of contiguous vowels "ee", which is of length 2.

If two or more strings in the array have maximum sub-strings of the same length, then the strings should remain in the order in which they were found in the orginal array.

FUNDAMENTALS
本卡塔的目标是编写一个函数，该函数将接收一个字符串数组作为其单一参数，
然后根据字符串中可能包含的单个最长的连续元音子串（aeiouAEIOU）的长度，
对每个字符串进行处理和排序（按降序）。

字符串可能包含字母、数字、特殊字符、大写、小写、空白，而且可能（通常会有）
多个连续元音的子串。我们只对输入数组中每个字符串中最长的一个元音子串感兴趣。

例子。

str1 = "今天真是个好日子"
str2 = "还不错，但是风很大"
当这些字符串被排序时，str1将排在第一位，因为它的最长的连续元音子串 "eau "的长度是3，
而str2的最长的连续元音子串 "ee "的长度是2。

如果数组中的两个或多个字符串有相同长度的最大子字符串，那么这些字符串应保持它们在初始数
组中的顺序。

基本原理
'''
word = "bananana"
i = word.find("na")
print(i)

# 645 -> 723  benchmark 5kyu -> 4kyu

def isVowels(x): # sperate not suit to 连续元音
    return [i for i in x if x.lower() in 'aeiou']

# Rank 12th by Eric 2021/0726
def isVowels(x): # 子函数统计连续元音字母切片长度
    return max(''.join([i if i.lower() in 'aeiou' else '-' for i in x]).split("-"),key=len)
x = "AIBoURH"
print(x.lower())
print(isVowels(x))

def sort_strings_by_vowels(seq):
    # your code here
    return sorted(seq,key=lambda x:len(isVowels(x)),reverse=True)

seq = ["AIBRH","","YOUNG","GREEEN"] # ["GREEEN","AIBRH","YOUNG",""]
print(sort_strings_by_vowels(seq))


#1st
import re
def sort_strings_by_vowels(seq):
    return sorted(seq, reverse=True, key=lambda x: max((len(i) for i in re.findall(r'[aeiouAEIOU]+', x)), default=0))

#2nd
import re
def sort_strings_by_vowels(seq):
    return sorted(seq, reverse=True, key=lambda s: max(map(len, re.findall('[aeiou]*', s, re.I))))


# rainbow

#from string import maketrans
rainbow_cn = "红橙黄绿蓝靛紫"
rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple']
s = dict(zip(rainbow,rainbow_cn))
print(s)

import string
#tabl = string.maketrans("aeiouAEIOU", "          ")
#string = string.translate(tabl)
print("string:",string)

import translate
from translate import Translator

LANGUAGES = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'ar': 'arabic',
    'be': 'belarusian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'zh-CN': 'chinese_simplified',
    'zh-TW': 'chinese_traditional',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'gl': 'galician',
    'de': 'german',
    'el': 'greek',
    'iw': 'hebrew',
    'hi': 'hindi',
    'hu': 'hungarian',
    'is': 'icelandic',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'ko': 'korean',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'mk': 'macedonian',
    'ms': 'malay',
    'mt': 'maltese',
    'no': 'norwegian',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'ro': 'romanian',
    'ru': 'russian',
    'sr': 'serbian',
    'sk': 'slovak',
    'sl': 'slovenian',
    'es': 'spanish',
    'sw': 'swahili',
    'sv': 'swedish',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'yi': 'yiddish',
  }

s = "Age does not make us childish, as men tell,It merely finds us children still at heart.Johann Wolfgang von Goethe. Faust"

#s_cn = translate.translate(s,cn)
'''

from googletrans import Translator

tran = Translator()
result = tran.translate('中国')
#print(result)

trans = Translator()
result = trans.translate('China', dest='zh-CN')
#print(result)

'''

