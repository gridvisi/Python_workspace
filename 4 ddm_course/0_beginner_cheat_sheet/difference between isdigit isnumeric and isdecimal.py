#7 kyu Convert an array of strings to array of numbers
'''
Some really funny web dev gave you a sequence of numbers from his API response as an sequence of strings!

You need to cast the whole array to the correct type.

Create the function that takes as a parameter a sequence of numbers represented as strings and outputs a sequence of numbers.

ie:["1", "2", "3"] to [1, 2, 3]

Note that you can receive floats as well.

'''
def to_float_array(arr):
    # your code here
    return [float(i) for i in arr]

def to_float_array(arr):
    return list(map(float, arr))


#What's the difference between str.isdigit, isnumeric and isdecimal

phil = "I am 11 years old and I am in K5 grade"
print('11'.isdecimal())
print('11'.isalnum())

phil_digit = []
phil_alnum = []
phil_num = []
phil_decim = []

for c in phil.split(" "):
    if c.isnumeric():
        phil_num.append(c)
    elif c.isdigit():
        phil_digit.append(c)
    elif c.isdecimal():
        phil_decim.append(c)
    elif c.isalnum():
        phil_alnum.append(c)
print(phil_num,phil_digit,phil_decim,phil_alnum)


#case 2nd study:
phil = "I am 11 years old and I am in K 5 grade"
#转换为字典格式存储phil的年龄和年级：{'age':11,'grade':"k5"}
#应该使用下列哪个内置函数？
phil_digit = []
phil_alnum = []
phil_num = []
phil_decim = []
phil_alpha = []
for c in phil.split(" "):
    if c.isnumeric():
        phil_num.append(c)
    if c.isdigit():
        phil_digit.append(c)
    if c.isdecimal():
        phil_decim.append(c)
    if c.isalnum():
        phil_alnum.append(c)
    if c.isalpha():
        phil_alpha.append(c)
print('2nd Case:',phil_num,phil_digit,phil_decim,phil_alnum,phil_alpha)

print(dict(zip(['age','grade'],phil_num)))



#case 3rd study:
phil = "I am 11 years old and I am in K 5 grade"
#转换为字典格式存储phil的年龄和年级：{'age':11,'grade':"k5"}
#应该使用下列哪个内置函数？
phil_digit = []
phil_alnum = []
phil_num = []
phil_decim = []
phil_alpha = []
for c in phil.split(" "):
    if c.isnumeric():
        phil_num.append(c)
    elif c.isdigit():
        phil_digit.append(c)
    elif c.isdecimal():
        phil_decim.append(c)
    elif c.isalnum():
        phil_alnum.append(c)
    elif c.isalpha():
        phil_alpha.append(c)
print('3rd Case:',phil_num,phil_digit,phil_decim,phil_alnum,phil_alpha)

print(dict(zip(['age','grade'],phil_num)))



# 4th case-study
# 输入改为列表格式，年龄->int, 年级为字符串形式的整数
phil = ['2021','I', 'am', 11, 'years', 'old','5','grade','45.5',39.2,'kg']

phil_digit = []
phil_alnum = []
phil_num = []
phil_decim = []
phil_int = []
phil_float = []
for c in phil:
    try:
        if c.isnumeric(): #
            #'int' object has no attribute 'isnumeric'
            phil_num.append(c)

        elif c.isdigit():
            phil_digit.append(c)
            # 'int' object has no attribute 'isdigit'

        elif c.isdecimal():
            phil_decim.append(c)

        elif c.isalnum():
                phil_alnum.append(c)
    except:
        if type(c) == int:
            phil_int.append(c)
            print(f"{c} is {type(c)}")
        elif type(c) == float:
            phil_float.append(c)

print('isnumberic:',phil_num)
print('isdigit:',phil_digit)
print('isdecimal:',phil_decim)
print('isalnum:',phil_alnum)
print('int:',phil_int)
print('float:',phil_float)


'''
s.isdigit()
s.isnumeric()
s.isdecimal()
'''

def spam(s):
    for attr in 'isnumeric', 'isdecimal', 'isdigit':
        print(attr, getattr(s, attr)())

spam('½')
'''
isnumeric True
isdecimal False
isdigit False
>>> spam('³')
isnumeric True
isdecimal False
isdigit True
'''

import sys
import unicodedata
from collections import defaultdict

d = defaultdict(list)
for i in range(sys.maxunicode + 1):
    s = chr(i)
    t = s.isnumeric(), s.isdecimal(), s.isdigit()
    if len(set(t)) == 2:
        try:
            name = unicodedata.name(s)
        except ValueError:
            name = f'codepoint{i}'
        print(s, name)
        d[t].append(s)

'''
+-------------+-----------+-------------+----------------------------------+
| isdecimal() | isdigit() | isnumeric() |          Example                 |
+-------------+-----------+-------------+----------------------------------+
|    True     |    True   |    True     | "038", "੦੩੮", "０３８"           |
|  False      |    True   |    True     | "⁰³⁸", "🄀⒊⒏", "⓪③⑧"          |
|  False      |  False    |    True     | "↉⅛⅘", "ⅠⅢⅧ", "⑩⑬㊿", "壹貳參"  |
|  False      |  False    |  False      | "abc", "38.0", "-38"             |
+-------------+-----------+-------------+----------------------------------+
'''

'''
Python文档中指出了这三种方法的区别。

str.isdigit
如果字符串中的所有字符都是数字，并且至少有一个字符，则返回真，否则返回假。
数字包括十进制字符和需要特殊处理的数字，如兼容上标数字。这涵盖了不能用来
组成以10为基数的数字的数字，如Kharosthi数字。从形式上看，数字是一个具
有Numeric_Type=Digit或Numeric_Type=Decimal属性值的字符。

str.isnumeric
如果字符串中的所有字符都是数字字符，并且至少有一个字符，则返回真，否则返
回假。数字字符包括数字字符，以及所有具有Unicode数值属性的字符，
例如U+2155, VULGAR FRACTION ONE FIFTH。从形式上看，数字字符是那些
具有Numeric_Type=Digit、Numeric_Type=Decimal或Numeric_Type=Numeric的属性值的字符。

str.isdecimal
如果字符串中的所有字符都是十进制字符并且至少有一个字符，则返回true，否则
返回false。十进制字符是那些可以用来组成以10为基数的数字的字符，
例如U+0660, ARABIC-INDIC DIGIT ZERO。从形式上看，十进制字符是Unicode
通用类别 "Nd "中的一个字符。

The Python documentation notes the difference between the three methods.

str.isdigit
Return true if all characters in the string are digits and there is at least one character, false otherwise. Digits include decimal characters and digits that need special handling, such as the compatibility superscript digits. This covers digits which cannot be used to form numbers in base 10, like the Kharosthi numbers. Formally, a digit is a character that has the property value Numeric_Type=Digit or Numeric_Type=Decimal.

str.isnumeric
Return true if all characters in the string are numeric characters, and there is at least one character, false otherwise. Numeric characters include digit characters, and all characters that have the Unicode numeric value property, e.g. U+2155, VULGAR FRACTION ONE FIFTH. Formally, numeric characters are those with the property value Numeric_Type=Digit, Numeric_Type=Decimal or Numeric_Type=Numeric.

str.isdecimal
Return true if all characters in the string are decimal characters and there is at least one character, false otherwise. Decimal characters are those that can be used to form numbers in base 10, e.g. U+0660, ARABIC-INDIC DIGIT ZERO. Formally a decimal character is a character in the Unicode General Category “Nd”.
'''


'''
By definition, isdecimal() ⊆ isdigit() ⊆ isnumeric(). That is, if a string is decimal, then it'll also be digit and numeric.

Therefore, given a string s and test it with those three methods, there'll only be 4 types of results.

+-------------+-----------+-------------+----------------------------------+
| isdecimal() | isdigit() | isnumeric() |          Example                 |
+-------------+-----------+-------------+----------------------------------+
|    True     |    True   |    True     | "038", "੦੩੮", "０３８"           |
|  False      |    True   |    True     | "⁰³⁸", "🄀⒊⒏", "⓪③⑧"          |
|  False      |  False    |    True     | "↉⅛⅘", "ⅠⅢⅧ", "⑩⑬㊿", "壹貳參"  |
|  False      |  False    |  False      | "abc", "38.0", "-38"             |
+-------------+-----------+-------------+----------------------------------+
1. Some examples of characters isdecimal()==True

(thus isdigit()==True and isnumeric()==True)

"0123456789"  DIGIT ZERO~NINE
"٠١٢٣٤٥٦٧٨٩"  ARABIC-INDIC DIGIT ZERO~NINE
"०१२३४५६७८९"  DEVANAGARI DIGIT ZERO~NINE
"০১২৩৪৫৬৭৮৯"  BENGALI DIGIT ZERO~NINE
"੦੧੨੩੪੫੬੭੮੯"  GURMUKHI DIGIT ZERO~NINE
"૦૧૨૩૪૫૬૭૮૯"  GUJARATI DIGIT ZERO~NINE
"୦୧୨୩୪୫୬୭୮୯"  ORIYA DIGIT ZERO~NINE
"௦௧௨௩௪௫௬௭௮௯"  TAMIL DIGIT ZERO~NINE
"౦౧౨౩౪౫౬౭౮౯"  TELUGU DIGIT ZERO~NINE
"೦೧೨೩೪೫೬೭೮೯"  KANNADA DIGIT ZERO~NINE
"൦൧൨൩൪൫൬൭൮൯"  MALAYALAM DIGIT ZERO~NINE
"๐๑๒๓๔๕๖๗๘๙"  THAI DIGIT ZERO~NINE
"໐໑໒໓໔໕໖໗໘໙"  LAO DIGIT ZERO~NINE
"༠༡༢༣༤༥༦༧༨༩"  TIBETAN DIGIT ZERO~NINE
"၀၁၂၃၄၅၆၇၈၉"  MYANMAR DIGIT ZERO~NINE
"០១២៣៤៥៦៧៨៩"  KHMER DIGIT ZERO~NINE
"０１２３４５６７８９"  FULLWIDTH DIGIT ZERO~NINE
"𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗"  MATHEMATICAL BOLD DIGIT ZERO~NINE
"𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡"  MATHEMATICAL DOUBLE-STRUCK DIGIT ZERO~NINE
"𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫"  MATHEMATICAL SANS-SERIF DIGIT ZERO~NINE
"𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵"  MATHEMATICAL SANS-SERIF BOLD DIGIT ZERO~NINE
"𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿"  MATHEMATICAL MONOSPACE DIGIT ZERO~NINE
2. Some examples of characters isdecimal()==False but isdigit()==True

(thus isnumeric()==True)

"⁰¹²³⁴⁵⁶⁷⁸⁹"  SUPERSCRIPT ZERO~NINE
"₀₁₂₃₄₅₆₇₈₉"  SUBSCRIPT ZERO~NINE
"🄀⒈⒉⒊⒋⒌⒍⒎⒏⒐"  DIGIT ZERO~NINE FULL STOP
"🄁🄂🄃🄄🄅🄆🄇🄈🄉🄊"  DIGIT ZERO~NINE COMMA
"⓪①②③④⑤⑥⑦⑧⑨"  CIRCLED DIGIT ZERO~NINE
"⓿❶❷❸❹❺❻❼❽❾"  NEGATIVE CIRCLED DIGIT ZERO~NINE
"⑴⑵⑶⑷⑸⑹⑺⑻⑼"  PARENTHESIZED DIGIT ONE~NINE
"➀➁➂➃➄➅➆➇➈"  DINGBAT CIRCLED SANS-SERIF DIGIT ONE~NINE
"⓵⓶⓷⓸⓹⓺⓻⓼⓽"  DOUBLE CIRCLED DIGIT ONE~NINE
"➊➋➌➍➎➏➐➑➒"  DINGBAT NEGATIVE CIRCLED SANS-SERIF DIGIT ONE~NINE
"፩፪፫፬፭፮፯፰፱"  ETHIOPIC DIGIT ONE~NINE
3. Some examples of characters isdecimal()==False and isdigit()==False but isnumeric()==True

"½⅓¼⅕⅙⅐⅛⅑⅒⅔¾⅖⅗⅘⅚⅜⅝⅞⅟↉"  VULGAR FRACTION
"৴৵৶৷৸৹"  BENGALI CURRENCY NUMERATOR
"௰௱௲"  TAMIL NUMBER TEN, ONE HUNDRED, ONE THOUSAND
"౸౹౺౻౼౽౾"  TELUGU FRACTION DIGIT
"൰൱൲൳൴൵"  MALAYALAM NUMBER, MALAYALAM FRACTION
"༳༪༫༬༭༮༯༰༱༲"  TIBETAN DIGIT HALF ZERO~NINE
"፲፳፴፵፶፷፸፹፺፻፼"  ETHIOPIC NUMBER TEN~NINETY, HUNDRED, TEN THOUSAND
"៰៱៲៳៴៵៶៷៸៹"  KHMER SYMBOL LEK ATTAK
"ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪⅫⅬⅭⅮⅯ"  ROMAN NUMERAL
"ⅰⅱⅲⅳⅴⅵⅶⅷⅸⅹⅺⅻⅼⅽⅾⅿ"  SMALL ROMAN NUMERAL
"ↀↁↂↅↆ"  ROMAN NUMERAL
"⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳㉑㉒㉓㉔㉕㉖㉗㉘㉙㉚㉛㉜㉝㉞㉟㊱㊲㊳㊴㊵㊶㊷㊸㊹㊺㊻㊼㊽㊾㊿"  CIRCLED NUMBER TEN~FIFTY
"㉈㉉㉊㉋㉌㉍㉎㉏"  CIRCLED NUMBER TEN~EIGHTY ON BLACK SQUARE
"⑽⑾⑿⒀⒁⒂⒃⒄⒅⒆⒇"  PARENTHESIZED NUMBER TEN~TWENTY
"⒑⒒⒓⒔⒕⒖⒗⒘⒙⒚⒛"  NUMBER TEN~TWENTY FULL STOP
"⓫⓬⓭⓮⓯⓰⓱⓲⓳⓴"  NEGATIVE CIRCLED NUMBER ELEVEN
"⓾➉❿➓"  various styles of CIRCLED NUMBER TEN
"🄌"  DINGBAT NEGATIVE CIRCLED SANS-SERIF DIGIT ZERO
"〇"  IDEOGRAPHIC NUMBER ZERO
"〡〢〣〤〥〦〧〨〩〸〹〺"  HANGZHOU NUMERAL ONE~TEN, TWENTY, THIRTY
"㆒㆓㆔㆕"  IDEOGRAPHIC ANNOTATION ONE~FOUR MARK
"㈠㈡㈢㈣㈤㈥㈦㈧㈨㈩"  PARENTHESIZED IDEOGRAPH ONE~TEN
"㊀㊁㊂㊃㊄㊅㊆㊇㊈㊉"  CIRCLED IDEOGRAPH ONE~TEN
"一二三四五六七八九十壹貳參肆伍陸柒捌玖拾零百千萬億兆弐貮贰㒃㭍漆什㐅陌阡佰仟万亿幺兩㠪亖卄卅卌廾廿"  CJK UNIFIED IDEOGRAPH
"參拾兩零六陸什"  CJK COMPATIBILITY IDEOGRAPH
"𐄇𐄈𐄉𐄊𐄋𐄌𐄍𐄎𐄏𐄐𐄑𐄒𐄓𐄔𐄕𐄖𐄗𐄘"  AEGEAN NUMBER ONE~NINE, TEN~NINETY
"𐄙𐄚𐄛𐄜𐄝𐄞𐄟𐄠𐄡𐄢𐄣𐄤𐄥𐄦𐄧𐄨𐄩𐄪"  AEGEAN NUMBER ONE~NINE HUNDRED, ONE~NINE THOUSAND
"𐄬𐄭𐄮𐄯𐄰𐄱𐄲𐄳"  AEGEAN NUMBER TEN~NINETY THOUSAND
"𐅀𐅁𐅂𐅃𐅆𐅇𐅈𐅉𐅊𐅋𐅌𐅍𐅎𐅏𐅐𐅑𐅒𐅓𐅔𐅕𐅖𐅗𐅘𐅙𐅚𐅛𐅜𐅝𐅞𐅟𐅠𐅡𐅢𐅣𐅤𐅥𐅦𐅧𐅨𐅩𐅪𐅫𐅬𐅭𐅮𐅯𐅰𐅱𐅲𐅳𐅴"  GREEK ACROPHONIC ATTIC
"𝍠𝍡𝍢𝍣𝍤𝍥𝍦𝍧𝍨"  COUNTING ROD UNIT DIGIT ONE~NINE
"𝍩𝍪𝍫𝍬𝍭𝍮𝍯𝍰𝍱"  COUNTING ROD TENS DIGIT ONE~NINE
'''